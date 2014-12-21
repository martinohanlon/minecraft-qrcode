from qrcode import *
from mcpi.minecraft import *
from mcpi.block import *

def getQR(inputString):
    qr = QRCode(version=1,
                error_correction=ERROR_CORRECT_L,
                border=1)
    qr.add_data(inputString)
    qr.make()
    return qr.get_matrix()

mc = Minecraft.create()
pos = mc.player.getTilePos()

qrMatrix = getQR("http://www.stuffaboutcode.com")

rowNo = 0
for row in qrMatrix:
    rowNo -= 1
    columnNo = 0
    for column in row:
        columnNo -= 1
        if column:
            #black
            blockColour = 15
        else:
            #white
            blockColour = 0

        mc.setBlock(pos.x + rowNo, pos.y + columnNo, pos.z, WOOL.id, blockColour)
