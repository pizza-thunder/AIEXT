import time

print("Type this sentence as fast as you can:")
text = "The quick brown fox jumps over the lazy dog"
print(text)

input("Press Enter to start: ")
start_time = time.time()

typed_text = input()

end_time = time.time()
total_time = end_time - start_time

correct = 0
incorrect = 0

for i in range(len(text)):
    if i >= len(typed_text):
        incorrect += len(text) - i
        break
    if typed_text[i] == text[i]:
        correct += 1
    else:
        incorrect += 1

accuracy = correct / len(text) * 100
wpm = len(typed_text) / 5 / (total_time / 60)

print("Your typing speed: {:.2f} WPM".format(wpm))
print("Accuracy: {:.2f}%".format(accuracy))
print("Total time: {:.2f} seconds".format(total_time))
