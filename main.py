import random
import os

def clear_screen():
    """Xóa màn hình (Windows hoặc macOS/Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words(filename):
    """Đọc file txt theo format: word:pronunciation:meaning"""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) >= 3:
                    word = parts[0].strip()
                    pron = parts[1].strip()
                    meaning = ':'.join(parts[2:]).strip()  # phòng trường hợp nghĩa có dấu ':'
                    words.append((word, pron, meaning))
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {filename}")
        exit()
    return words

def mode_word_to_meaning(words):
    """1️⃣ Hiển thị từ → đoán nghĩa và phát âm"""
    while True:
        clear_screen()
        word, pron, meaning = random.choice(words)
        print(f"Từ: {word}")
        inp = input("\nNhấn Enter để xem đáp án, hoặc nhập phím bất kỳ để quay lại menu: ")
        if inp.strip() != "":
            break
        print(f"👉 Phiên âm: {pron}")
        print(f"👉 Nghĩa: {meaning}")
        input("\nNhấn Enter để tiếp tục...")

def mode_meaning_to_word(words):
    """2️⃣ Hiển thị nghĩa → đoán từ và phát âm"""
    while True:
        clear_screen()
        word, pron, meaning = random.choice(words)
        print(f"Nghĩa: {meaning}")
        inp = input("\nNhấn Enter để xem đáp án, hoặc nhập phím bất kỳ để quay lại menu: ")
        if inp.strip() != "":
            break
        print(f"👉 Từ: {word}")
        print(f"👉 Phiên âm: {pron}")
        input("\nNhấn Enter để tiếp tục...")

def mode_pronunciation(words):
    """3️⃣ Hiển thị phát âm → đoán từ và nghĩa"""
    while True:
        clear_screen()
        word, pron, meaning = random.choice(words)
        print(f"Phát âm: {pron}")
        inp = input("\nNhấn Enter để xem đáp án, hoặc nhập phím bất kỳ để quay lại menu: ")
        if inp.strip() != "":
            break
        print(f"👉 Từ: {word}")
        print(f"👉 Nghĩa: {meaning}")
        input("\nNhấn Enter để tiếp tục...")

def main():
    words = load_words('vocabs.txt')
    while True:
        clear_screen()
        print("=== 📘 Luyện từ vựng tiếng Anh ===\n")
        print("1. Hiển thị TỪ → đoán NGHĨA (và phát âm)")
        print("2. Hiển thị NGHĨA → đoán TỪ (và phát âm)")
        print("3. Hiển thị PHÁT ÂM → đoán TỪ & NGHĨA")
        print("4. Thoát chương trình")
        choice = input("\nChọn (1/2/3/4): ").strip()
        
        if choice == '1':
            mode_word_to_meaning(words)
        elif choice == '2':
            mode_meaning_to_word(words)
        elif choice == '3':
            mode_pronunciation(words)
        elif choice == '4':
            print("\nTạm biệt 👋 Hẹn gặp lại!")
            break
        else:
            input("\nLựa chọn không hợp lệ. Nhấn Enter để thử lại...")

if __name__ == "__main__":
    main()
