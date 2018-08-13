from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

_VERSION = '0.1.0'

# 創建主視窗
window = Tk()
window.title("聖槍刺擊 " + _VERSION)

class NewEntry:
    def __init__ (self, labelText, column, row):
        self.newObject = {}
        self.newObject['label'] = ttk.Label(window, text = labelText)
        self.newObject['label'].grid(column = column, row = row)
        self.newObject['value'] = StringVar()
        self.newObject['entry'] = ttk.Entry(window, width = 4, textvariable = self.newObject['value'])
        self.newObject['entry'].grid(column = column + 1, row = row)

    def get (self):
        return int(self.newObject['value'].get())

# 第一列 素質
strength = NewEntry("STR：", 0, 0)
intelligence = NewEntry("INT：", 2, 0)

# 第二列 素質ATK+修鍊ATK
baseAtk = NewEntry("素質ATK：", 0, 1)
repairAtk = NewEntry("修鍊ATK：", 2, 1)

# 第三列 武器
weaponAtk = NewEntry("武器ATK：", 0, 2)
weaponLevel = NewEntry("武器等級：", 2, 2)
intensify = NewEntry("武器精鍊值：", 4, 2)

# 第四、五列 ATK增益效果
itemAtk = NewEntry("卡裝ATK：", 0, 3)
classAtk = NewEntry("階級&atk(%)：", 2, 3)
raceAtk = NewEntry("種族(%)：", 0, 4)
enemyAttribute = NewEntry("敵方屬性(%)：", 2, 4)

# 第六列 素質MATK+武器MATK
baseMatk = NewEntry("素質MATK：", 0, 5)
weaponMatk = NewEntry("武器MATK：", 2, 5)

# 第七列 武器MATK+卡裝ATK
itemMatk = NewEntry("卡裝MATK：", 0, 6)

# 第八、九列 MATK增益效果
enchant = NewEntry("卡裝&附魔(%)：", 0, 7)
raceMatk = NewEntry("種族&針對魔物(%)：", 2, 7)
enemyAttributeForMagic = NewEntry("敵方屬性(%)：", 0, 8)
myAttributeForMagic = NewEntry("自身屬性(%)：", 2, 8)

# 第十列 技能增傷
skill = NewEntry("技能(%)：", 0, 9)

# 第十一行 計算結果
def CalculateDamage ():
    firstAtk = repairAtk.get() + baseAtk.get() * 2
    secondAtk = weaponAtk.get() * (1 + strength.get() * 0.005 + weaponLevel.get() * 0.05) + 5 * intensify.get() + 8 * (intensify.get() + weaponLevel.get() - 8) + 18 * weaponLevel.get() + itemAtk.get()
    secondAtkBuff = (1 + classAtk.get() / 100) * (1 + raceAtk.get() / 100) * (1 + enemyAttribute.get() / 100)
    secondMatk = (weaponMatk.get() + 5 * intensify.get()) * (1 + 0.1 * weaponLevel.get()) + 8 * (intensify.get() + weaponLevel.get() - 8)
    secondMatkBuff = (1 + enchant.get() / 100) * (1 + raceMatk.get() / 100) * (1 + enemyAttributeForMagic.get() / 100) * (1 + myAttributeForMagic.get() / 100)

    return ((firstAtk + secondAtk * secondAtkBuff) * 8.75 + 4 * secondMatk * secondMatkBuff * ((5 * intelligence.get() / 100 + 2.5) * 1.75 + 1.8)) * (1 + skill.get() / 100)

def CalculateAction():
    damage = str(CalculateDamage())
    calculationLabel.config(text = damage)

calculation = ttk.Button(window, text = "計算", command = CalculateAction)
calculation.grid(column = 3, row = 10)
calculationLabel = ttk.Label(window, text = "")
calculationLabel.grid(column = 1, row = 10)

# 顯示主視窗
window.mainloop()