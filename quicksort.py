def quicksort(sequenza):
    if len(sequenza) <= 1:
        return sequenza
    else:
        #si prende il primo non avendo info a priori su come son fatte le liste
        pivot = sequenza[0]
        #divido la sequenza secondo il pivot
        #sequenza_smaller = []
        #sequenza_pivot = []
        #sequenza_larger = []
        #for element in sequenza:
        #    if element < pivot:
        #        sequenza_smaller.append(element)
        #    elif element == pivot:
        #        sequenza_pivot.append(element)
        #    else:
        #        sequenza_larger.append(element)
        sequenza_smaller = [n for n in sequenza if n<pivot]
        sequenza_pivot = [n for n in sequenza if n==pivot]
        sequenza_larger = [n for n in sequenza if n>pivot]
        return (quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger))

if __name__ == "__main__":
    sequenza = [9,3,2,6,8,5,199]
    print(quicksort(sequenza))