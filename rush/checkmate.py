def checkmate(board):  
    board_rows = board.splitlines()  # แยกกระดานออกเป็นแต่ละแถว

    # ตรวจสอบว่าทุกแถวมีความกว้างเท่ากัน
    board_width = len(board_rows[0])  # กำหนดความกว้างจากแถวแรก
    i = 0
    while i < len(board_rows):  # วนลูปเช็กทุกแถว
        if len(board_rows[i]) != board_width:  # ถ้าความกว้างไม่เท่ากัน
            print("Fail")  # แจ้งว่าไม่ผ่าน
            return  # ออกจากฟังก์ชัน
        i += 1

    # หาตำแหน่งของคิง
    king_loc = next(((i, row.index('K')) for i, row in enumerate(board_rows) if 'K' in row), None)  
    
    if not king_loc:  # ถ้าไม่มีคิงบนกระดาน
        print("Error")  # แจ้งว่า Error
        return  # ออกจากฟังก์ชัน

    x, y = king_loc  # เก็บพิกัดของคิง

    # ฟังก์ชันเช็กว่าคิงโดนโจมตีจากทิศทางที่กำหนดหรือไม่
    def is_under_attack_in_direction(dx, dy, pieces):
        i, j = x + dx, y + dy  # เริ่มเช็กจากตำแหน่งถัดไปในทิศที่กำหนด
        while 0 <= i < len(board_rows) and 0 <= j < len(board_rows[0]):  # ตรวจสอบว่าตำแหน่งยังอยู่ในกระดาน
            if board_rows[i][j] in pieces:  # ถ้าพบตัวหมากที่สามารถโจมตีคิงได้
                return True  # คิงกำลังถูกโจมตี
            if board_rows[i][j] != '.':  # ถ้ามีตัวหมากอื่นขวางอยู่
                break  # หยุดเช็ก
            i, j = i + dx, j + dy  # เลื่อนไปตำแหน่งถัดไปในทิศเดียวกัน
        return False  # ไม่มีการโจมตี

    # เช็กว่าคิงโดนเบี้ยโจมตีหรือไม่
    if x + 1 < len(board_rows) and ((y - 1 >= 0 and board_rows[x + 1][y - 1] == 'P') or (y + 1 < board_width and board_rows[x + 1][y + 1] == 'P')):
        print("Success")  # คิงโดนโจมตี
        return

    # เช็กว่าโดนเรือ (R) หรือราชินี (Q) โจมตีแนวตรงหรือแนวนอนหรือไม่
    if any(is_under_attack_in_direction(dx, dy, {'R', 'Q'}) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        print("Success")  # คิงโดนโจมตี
        return

    # เช็กว่าโดนบิชอป (B) หรือราชินี (Q) โจมตีแนวทแยงหรือไม่
    if any(is_under_attack_in_direction(dx, dy, {'B', 'Q'}) for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]):
        print("Success")  # คิงโดนโจมตี
        return

    print("Fail")  # ถ้าไม่มีตัวหมากไหนโจมตีคิงได้