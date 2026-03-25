class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


# персонажи
class GlowStreamer(Streamer, Mutant):
    def live(self):
        return super().live()

    def ultimate_content(self):
        return f"{self.earn()}. {self.superpower()}"


class ViralCyborg(TikToker, Mutant):
    def live(self):
        return super().live()

    def ultimate_content(self):
        return f"{self.viral()} {self.superpower()}"


class DonateMage(Streamer, TikToker):
    def live(self):
        return super().live()

    def ultimate_content(self):
        return f"{self.earn()}. {self.viral()}"


# MRO
print(f"GlowStreamer: {GlowStreamer.mro()}")
print(f"ViralCyborg: {ViralCyborg.mro()}")
print(f"DonateMage: {DonateMage.mro()}")
print()


# вывод метода live()
# по аналогии с duck = Duck()
gs = GlowStreamer()
vc = ViralCyborg()
dm = DonateMage()

print(gs.live())    # Стример
print(vc.live())     # Тиктокер
print(dm.live())      # Стример

# Почему так? Потому, что структурное программирование идёт слева-направо и сверху-вниз.
# А MRO при необходимости может идти направо, и подниматься наверх.
# Например, Python не находит у GlowStreamer'а свой live, и поднимается наверх (к super()).
# Первым находится класс Streamer (слева), а затем уже класс Mutant (справа). А object - очевидно, необходимый метод.
# Но т.к. Python нужен только один метод live(), то он берёт и останавливается на Streamer.

# GlowStreamer: GlowStreamer -> Streamer -> Mutant -> object
# ViralCyborg: ViralCyborg -> TikToker -> Mutant -> object
# DonateMage: DonateMage -> Streamer -> TikToker -> object

print()


# комбинированные способности
print(gs.ultimate_content())
print(vc.ultimate_content())
print(dm.ultimate_content())
