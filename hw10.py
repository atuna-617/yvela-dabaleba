def merge_sort(arr):
    if len(arr) > 1:
        #მასივი გავყოთ ორ ნაწილად
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #რეკურსიულად დავალაგოთ ორივე ნახევარი
        merge_sort(left_half)
        merge_sort(right_half)

        #შევაერთოთ დალაგებული ნახევრები
        i = j = k = 0

        #დააკოპირეთ მონაცემები დროებით სიებში left_half და right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        #შევამოწმოთ დარჩენილი ელემეტები
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#მაგალითი
arr = [38, 27, 43, 3, 9, 82, 10]
print("ორიგინალური განლაგება:", arr)

merge_sort(arr)
print("დაწყობილი განლაგება:", arr)
