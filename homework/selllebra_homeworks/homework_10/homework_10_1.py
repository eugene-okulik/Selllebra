def task_finished(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result
    return wrapper


@task_finished
def mood():
    your_mood = input('How are you?')
    print(f'Your mood is{your_mood}')


mood()
