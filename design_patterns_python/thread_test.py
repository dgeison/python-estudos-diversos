import threading
from singleton1_2 import Singleton

N_THREADS = 100
ids = set()


def create_instance():
    BARRIER = threading.Barrier(
        N_THREADS
    )  # Garante que todas as threads criem a instância ao mesmo tempo
    instance = Singleton()
    ids.add(id(instance))


def main():
    global ids
    ids = set()
    threads = []
    # Cria várias threads para tentar criar instâncias simultaneamente
    for _ in range(N_THREADS):
        thread = threading.Thread(target=create_instance)
        threads.append(thread)

    # Inicia as threads
    for thread in threads:
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    r = 1
    while len(ids) <= 1:
        Singleton._instancia = None
        main()
        r = r + 1
    print(f"Parou na execução: {r} com {len(ids)} instâncias")
