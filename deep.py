user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
list_of_correct_answers = ["42","forty-two","forty two"]
print("Yes" if user_answer in list_of_correct_answers else "No")