#sprint 5

def dp_change(coin_values, change, known_results):

    for cents in range(change+1):


        coin_count = cents

        for j in [c for c in coin_values if c <= cents]:

            print(known_results)
            if known_results[cents-j] + 1 < coin_count:
                coin_count = known_results[cents-j]+1

            known_results[cents] = coin_count

    return known_results[change]


def main():
    coin_values = [1, 2, 3]
    known_results = []
    change = 21
    dp_change(coin_values, change, known_results)
main()
