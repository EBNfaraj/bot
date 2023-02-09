from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5675510670:AAH9NCwSTOlHoVDX1pEEqInL_WjzTPsdQ0o"  # Bot toekn
ADMINS = [184557560]  # adminlar ro'yxati
#IP = env.str("ip")  # Xosting ip manzili
