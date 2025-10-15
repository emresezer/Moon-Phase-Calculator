moon_phases = [
    "Yeni Ay",        # 1
    "Hilal",          # 2
    "İlk Dördün",     # 3
    "Şişkin Hilal",   # 4
    "Dolunay",        # 5
    "Azalan Dolunay", # 6
    "Son Dördün",     # 7
    "Azalan Hilal"    # 8
]
print("Ay evreleri:")
for i, phase in enumerate(moon_phases):
    print(f"{i+1}. {phase}")
current_phase = int(input("Bugünkü ay evresi (1=Yeni Ay, 8=Azalan Hilal): "))
if current_phase < 1 or current_phase > 8:
    print("Hatalı giriş! 1 ile 8 arasında bir sayı girin.")
    exit()
days_later = int(input("Kaç gün sonrasını öğrenmek istiyorsunuz?: "))
phase_length = 29.53 / 8
phases_passed = int(days_later / phase_length)
future_phase_index = (current_phase - 1 + phases_passed) % 8
print(f"{days_later} gün sonra ay evresi: {moon_phases[future_phase_index]}")
