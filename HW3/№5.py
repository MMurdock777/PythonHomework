violator_songs = [
    ['World in My Eyes', 4,86],
    ['Sweetest Perfection', 4,43],
    ['Personal Jesus', 4,56],
    ['Halo', 4,9],
    ['Waiting for the Night', 6,7],
    ['Enjoy the Silence', 4,20],
    ['Policy of Truth', 4,76],
    ['Blue Dress', 4,29],
    ['Clean', 5,83]
]

num_songs = int(input("Сколько песен выбрать? "))
sum_length = 0
for i in range(0, num_songs):
    song_name = input(f"Название {i+1}-й песни:")
    for j in range(0, len(violator_songs)-1):
        if violator_songs[j][0] == song_name:
            sum_length += float(violator_songs[j][1]) + 0.01 * float(violator_songs[j][2])
            print(sum_length)

print(f"Общее время звучания песен: {sum_length}")