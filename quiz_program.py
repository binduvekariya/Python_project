# dictionary inside dictionary.. one key have one value-> this value is other dictionary
quiz = {
    "question1":
    {
        "question":"what is the capital of France ?",
        "answer": "Paris"
    },
    "question2":
    {
        "question":"what is the capital of Germany ?",
        "answer": "Berlin"
    },
    "question3":
    {
        "question":"what is the capital of Itly ?",
        "answer": "Rome"
    },
    "question4":
    {
        "question":"what is the capital of Spain ?",
        "answer": "Madrid"
    },
    "question5":
    {
        "question":"what is the capital of Portugal ?",
        "answer": "Lisbon"
    },
    "question6":
    {
        "question":"what is the capital of Switzerland ?",
        "answer": "Bern"
    },
    "question7":
    {
        "question":"what is the capital of Austria ?",
        "answer": "Vienna"
    }

}

score = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("answer? : ")
    
    if answer.lower()==value["answer"].lower():
        print("correct")
        score = score + 1
        print("your score is: "+ str(score))
        print(" ")

    else:
        print("incorrect!")
        print("the answer is: "+ value["answer"])
        print("your score is: "+ str(score))
        print(" ")


print("you got "+ str(score)+ " out of 7 correctly answer")
print("your percentage is "+ str(int(score/7 * 100)) + "%")
