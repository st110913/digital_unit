# 包 digital_unit 1.6b1
（language：Chinese）

这是一个有关**数据的单位**的包,如长度、面积、体积等，可以用它来表示一个数量的单位
使用示例
``` python
from digital_unit import CentiMeter,MilliMeters
from digital_unit import Number

if __name__ == '__main__':
    _1cm = Number(1.0, CentiMeter()) # Create the data. Don't forget the parentheses!
    print(_1cm)
    _1cm.change_unit(MilliMeter()) # Changes to the unit. Don't forget the parentheses!
    print(_1cm)
```
使用`Number(NUMBER, UNIT())`来创建实例，使用`XXX.change_unit(NEWUNIT())`来修改单位。
## 1.6b1版本新增
修改了导入方式。

## 1.6b1版本修正
无

# package digital_unit 1.6b1
(language: English)

This is **a unit of data** related to packages, such as length, area, volume, etc., it can be used to represent a number of units
Use the sample
```python
from digital_unit import CentiMeter,MilliMeters
from digital_unit import Number

if __name__ == "__main__" :
_1cm = Number(1.0,CentiMeter()) # Create the data. Don 't forget the parentheses.
print(_1cm)
_1cm.Change_unit(MilliMeter()) #Changes to the unit. Don 't forget the parentheses.
print(_1cm)
```
Using ` Number(NUBER, UNIT()) ` to create an instance, use ` XXX.Change_unit(NEWUNIT ()) ` to modify the UNIT

## Added in version 1.6b1
Modified the import method.

## Corrected in version 1.6b1
None