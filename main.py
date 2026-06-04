from src.preprocess import preprocess_chat

def main():
    f = open('data/SS.txt', 'r', encoding='utf-8')
    chat = f.read()
    print(preprocess_chat(chat))
    f.close()

if __name__ == '__main__':
    main()


