from oracle.logic import get_answer


MAX_QUESTIONS = 100


class TooManyQuestionAsked(Exception):
    questions_asked: int

    def __init__(self, questions_asked: int, *args: object) -> None:
        self.questions_asked = questions_asked
        super().__init__(*args)


def main() -> None:
    try:
        app_flow()
        print('Please come back another time.', end='\n')
    except TooManyQuestionAsked:
        print("Too many questions asked. Please try again later")
    except KeyboardInterrupt:
        print('Process terminated due to keyboard interrupt')


def app_flow() -> None:
    print("Welcome. I am the oracle. I will answer all question. But beware! You may not like what you hear.", end='\n\n')

    for n in range(1, MAX_QUESTIONS+1):
        userinput = input("Please enter a question - (provide 'quit' to exit): ").strip()
        if not userinput or userinput.lower() == 'quit':
            return
        if not isvalid(userinput):
            print("Sorry! Invalid question detected.", end='\n\n')
            continue
        print(f"The answer to your question is: \"{get_answer()}\"", end='\n\n')

    raise TooManyQuestionAsked(n)


# To-Do: Make a proper validator
def isvalid(_: str) -> bool:
    return True


if __name__ == '__main__':
    main()
