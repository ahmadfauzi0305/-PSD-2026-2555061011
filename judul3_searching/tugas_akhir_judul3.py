def sequential_search(kontak, n, target):
    i = 0
    counter = 0
    
    while i < n:
        if kontak[i]["nama"].lower() == target.lower():
            print(f"Kontak ditemukan: {kontak[i]['nama']} - {kontak[i]['nomor']}")
            counter += 1
        i += 1
        
    return counter


def main():
    kontak = [
        {"nama": "Fauzi", "nomor": "081234567890"},
        {"nama": "Ahmad", "nomor": "082345678901"},
        {"nama": "oji", "nomor": "083456789012"},
        {"nama": "uzi", "nomor": "084567890123"},
        {"nama": "stipen", "nomor": "085678901234"},
        {"nama": "kamad", "nomor": "087654321000"}
    ]
    
    n = len(kontak)
    
    print("Daftar Kontak:")
    for k in kontak:
        print(f"{k['nama']} - {k['nomor']}")
    
    target = input("\nMasukkan nama kontak yang ingin dicari: ")
    
    counter = sequential_search(kontak, n, target)
    
    if counter > 0:
        print(f"\nKontak dengan nama '{target}' ditemukan sebanyak {counter} kali.")
    else:
        print(f"\nKontak dengan nama '{target}' ngga ditemukan.")


if __name__ == "__main__":
    main()