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
    king_loc = None
    i = 0
    while i < len(board_rows) and not king_loc:
        if 'K' in board_rows[i]:
            king_loc = (i, board_rows[i].index('K'))
        i += 1

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
    if x + 1 < len(board_rows):
        if y - 1 >= 0 and board_rows[x + 1][y - 1] == 'P':
            print("Success")  # คิงโดนโจมตี
            return
        if y + 1 < board_width and board_rows[x + 1][y + 1] == 'P':
            print("Success")  # คิงโดนโจมตี
            return

    # เช็กว่าโดนเรือ (R) หรือราชินี (Q) โจมตีแนวตรงหรือแนวนอนหรือไม่
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    direction_idx = 0
    while direction_idx < len(directions):
        dx, dy = directions[direction_idx]
        if is_under_attack_in_direction(dx, dy, {'R', 'Q'}):
            print("Success")  # คิงโดนโจมตี
            return
        direction_idx += 1

    # เช็กว่าโดนบิชอป (B) หรือราชินี (Q) โจมตีแนวทแยงหรือไม่
    directions_diag = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    direction_diag_idx = 0
    while direction_diag_idx < len(directions_diag):
        dx, dy = directions_diag[direction_diag_idx]
        if is_under_attack_in_direction(dx, dy, {'B', 'Q'}):
            print("Success")  # คิงโดนโจมตี
            return
        direction_diag_idx += 1

    print("Fail")  # ถ้าไม่มีตัวหมากไหนโจมตีคิงได้
