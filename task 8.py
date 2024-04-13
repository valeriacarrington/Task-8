def maximize_income(N, C, gains, prices):
    laptops = [(i, gains[i], prices[i]) for i in range(len(gains))]
    laptops.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_gains = 0
    for laptop in laptops:
        if N == 0 or C < laptop[2]:
            break
        total_gains += laptop[1]
        C -= laptop[2]
        N -= 1

    return C + total_gains

# Example usage
N = 3
C = 10
gains = [5, 10, 15, 20]
prices = [3, 5, 7, 10]
print("Capital at the end of the summer:", maximize_income(N, C, gains, prices))
