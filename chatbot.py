import subprocess
import os

# Windows için encoding ayarla
if os.name == 'nt':  # Windows
    os.system('chcp 65001 >nul 2>&1')


def test_ollama():
    """Ollama'nın çalışıp çalışmadığını test et"""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        if result.returncode == 0:
            print("✅ Ollama çalışıyor!")
            return True
        else:
            print("❌ Ollama çalışmıyor!")
            return False
    except Exception as e:
        print(f"❌ Ollama hatası: {e}")
        return False


def ollama_chat(message, model="gemma:2b"):
    """Ollama ile sohbet etmek için fonksiyon"""
    try:
        # Sorunun dilini algıla ve aynı dilde cevap ver
        is_turkish = any(char in message.lower() for char in ['ç', 'ğ', 'ı', 'ş', 'ü', 'ö']) or any(
            word in message.lower() for word in ['ne', 'nedir', 'kimdir', 'nasıl', 'nerede', 'ne zaman'])

        if is_turkish:
            simple_prompt = f"Türkçe cevap ver: {message}"
        else:
            simple_prompt = f"Answer in English: {message}"

        result = subprocess.run(
            ["ollama", "run", model, simple_prompt],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=30
        )
        if result.returncode == 0:
            response = result.stdout.strip()
            # Boş cevap kontrolü
            if not response:
                return "Bot şu anda cevap veremiyor, lütfen tekrar deneyin."
            return response
        else:
            return "Model hatası: Lütfen soruyu tekrar sorun."
    except subprocess.TimeoutExpired:
        return "Zaman aşımı! Lütfen daha kısa bir soru sorun."
    except Exception as e:
        return f"Hata: Lütfen soruyu tekrar sorun."


def main():
    print("=" * 50)
    print("SOHBET BOTU")
    print("=" * 50)

    # Ollama test et
    if not test_ollama():
        print("\nÖnce şu komutu çalıştır:")
        print("ollama pull gemma:2b")
        input("\nDevam etmek için Enter'a bas...")
        return

    print("\nTarih, sanat ve sinema hakkında konuşabiliriz!")
    print("Çıkmak için 'quit' yazabilirsin.\n")

    # Ana sohbet döngüsü
    while True:
        try:
            # Kullanıcı girişi
            user_input = input("Sen: ")

            # Çıkış kontrolü
            if user_input.lower() in ['quit', 'exit', 'cik', 'q']:
                print("\nHoşça kal!\n")
                break

            # Boş girdi kontrolü
            if not user_input.strip():
                continue

            # Bot cevabı
            print("\nBot düşünüyor...")
            response = ollama_chat(user_input)
            print(f"Bot: {response}\n")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\n\nProgram sonlandırıldı!\n")
            break
        except Exception as e:
            print(f"\nBir hata oluştu: {str(e)}\n")


if __name__ == "__main__":  # Hata düzeltildi
    main()
