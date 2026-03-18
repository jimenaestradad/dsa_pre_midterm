from ll import LinkedList, Node

SONGS = [
    ("Tití Me Preguntó", "Bad Bunny", "Un Verano Sin Ti"),
    ("Me Porto Bonito", "Bad Bunny", "Un Verano Sin Ti"),
    ("Ojitos Lindos", "Bad Bunny", "Un Verano Sin Ti"),
    ("Moscow Mule", "Bad Bunny", "Un Verano Sin Ti"),
    ("Efecto", "Bad Bunny", "Un Verano Sin Ti"),
    ("Neverita", "Bad Bunny", "Un Verano Sin Ti"),
    ("Callaíta", "Bad Bunny", "YHLQMDLG"),
    ("Safaera", "Bad Bunny", "YHLQMDLG"),
    ("Yo Perreo Sola", "Bad Bunny", "YHLQMDLG"),
    ("La Canción", "Bad Bunny", "Oasis"),
    ("Amorfoda", "Bad Bunny", "X 100PRE"),
    ("Ni Bien Ni Mal", "Bad Bunny", "X 100PRE"),
    ("DÁKITI", "Bad Bunny", "El Último Tour del Mundo"),
    ("La Noche de Anoche", "Bad Bunny", "El Último Tour del Mundo"),
    ("Yonaguni", "Bad Bunny", "Single"),
    ("Un Preview", "Bad Bunny", "Single"),
    ("Where She Goes", "Bad Bunny", "Single"),
    ("Un Ratito", "Bad Bunny", "Un Verano Sin Ti"),
    ("Party", "Bad Bunny", "Un Verano Sin Ti"),
    ("Tarot", "Bad Bunny", "Un Verano Sin Ti"),
    ("High", "Rawayana", "Trippy Caribbean"),
    ("Sin Ti", "Rawayana", "Trippy Caribbean"),
    ("Feriado", "Rawayana", "Licencia Para Ser Libre"),
    ("Binikini", "Rawayana", "Licencia Para Ser Libre"),
    ("Algo Distinto", "Rawayana", "Licencia Para Ser Libre"),
    ("Véngase", "Rawayana", "Rawayanaland"),
    ("Into You", "Rawayana", "Rawayanaland"),
    ("Camarones y Vinito", "Rawayana", "Rawayanaland"),
    ("Welcome to el Sur", "Rawayana", "Rawayanaland"),
    ("Dame un Break", "Rawayana", "Licencia Para Ser Libre"),
    ("drivers license", "Olivia Rodrigo", "SOUR"),
    ("good 4 u", "Olivia Rodrigo", "SOUR"),
    ("deja vu", "Olivia Rodrigo", "SOUR"),
    ("traitor", "Olivia Rodrigo", "SOUR"),
    ("happier", "Olivia Rodrigo", "SOUR"),
    ("brutal", "Olivia Rodrigo", "SOUR"),
    ("vampire", "Olivia Rodrigo", "GUTS"),
    ("bad idea right?", "Olivia Rodrigo", "GUTS"),
    ("get him back!", "Olivia Rodrigo", "GUTS"),
    ("all-american bitch", "Olivia Rodrigo", "GUTS"),
    ("Espresso", "Sabrina Carpenter", "Short n' Sweet"),
    ("Please Please Please", "Sabrina Carpenter", "Short n' Sweet"),
    ("Feather", "Sabrina Carpenter", "emails i can't send"),
    ("Nonsense", "Sabrina Carpenter", "emails i can't send"),
    ("because i liked a boy", "Sabrina Carpenter", "emails i can't send"),
    ("Skinny Dipping", "Sabrina Carpenter", "emails i can't send"),
    ("Fast Times", "Sabrina Carpenter", "emails i can't send"),
    ("Thumbs", "Sabrina Carpenter", "EVOLution"),
    ("Sue Me", "Sabrina Carpenter", "Singular: Act I"),
    ("Almost Love", "Sabrina Carpenter", "Singular: Act I"),
    
]

def build_playlist(song_tuples):
    ll = LinkedList()
    for title, artist, album in song_tuples:
        node = Node(title, artist, album)
        ll.insert_at_end(node)
    return ll


def print_sample(ll):
    print("\nResumen de la playlist:")
    print("Total canciones:", len(ll))

    print("\nPrimeras 3 canciones:")
    idx = 0
    for node in ll:
        if idx < 3:
            print(f"{idx+1}. {node.data.get('title')} - {node.data.get('artist')} ({node.data.get('album')})")
        idx += 1
        if idx >= 3:
            break

    last = None
    for node in ll:
        last = node
    if last is not None:
        print("\nÚltimas 3 canciones (desde el final hacia atrás):")
        back = last
        back_idx = 0
        while back is not None and back_idx < 3:
            print(f"{back_idx+1}. {back.data.get('title')} - {back.data.get('artist')} ({back.data.get('album')})")
            back = back.prev
            back_idx += 1


def quick_link_check(ll):
    nodes = []
    for node in ll:
        nodes.append(node)
    ok_forward = all(nodes[i].next is nodes[i+1] for i in range(len(nodes)-1)) if len(nodes) > 1 else True
    ok_backward = all(nodes[i+1].prev is nodes[i] for i in range(len(nodes)-1)) if len(nodes) > 1 else True
    print("\nChequeo de enlaces:")
    print("Forward OK:", ok_forward)
    print("Backward OK:", ok_backward)


def main():
    playlist = build_playlist(SONGS)
    print_sample(playlist)
    quick_link_check(playlist)
   
    print("\nPlaylist cargada y lista para usarse en la interfaz (siguiente paso).")

if __name__ == "__main__":
    main()