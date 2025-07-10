# 시간을 초단위로 변경하는 함수
def change_clock_sceond(clock):
    min, sec = clock.split(":")
    second_clcok = (int(min) * 60) + int(sec) 
    return second_clcok

# 시간을 "mm:ss"로 변경
def change_clock(result):
    min_str = (result // 60)
    if min_str < 10:
        min_str = "0"+ str(min_str)
        
    sec_str = (result % 60)
    if sec_str < 10:
        sec_str = "0"+ str(sec_str)
    
    print(type(min_str), type(sec_str))
    result_d = min_str + ":" + sec_str
    print(result_d)
    return min_str+":"+sec_str
        
def solution(video_len, pos, op_start, op_end, commands):
    #1. 시간을 초단위로 변경
    op_start = change_clock_sceond(op_start)
    op_end = change_clock_sceond(op_end)
    video_len = change_clock_sceond(video_len)
    pos = change_clock_sceond(pos)
    
    if pos >= op_start and pos <= op_end:
            pos = op_end
            pass
            
    for command in commands:    
        if command == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        elif command == "next":
            if (video_len - pos) < 10:
                pos = video_len
            else:
                pos += 10 
                
        if pos >= op_start and pos <= op_end:
            pos = op_end
            pass
        
    return change_clock(pos)

# def solution(video_len, pos, op_start, op_end, commands):
#     # 시간 문자열을 초로 변환
#     def time_to_seconds(t):
#         m, s = map(int, t.split(":"))
#         return m * 60 + s

#     # 초를 시간 문자열로 변환
#     def seconds_to_time(sec):
#         m, s = divmod(sec, 60)
#         return f"{m:02}:{s:02}"

#     video_sec = time_to_seconds(video_len)
#     pos_sec = time_to_seconds(pos)
#     start_sec = time_to_seconds(op_start)
#     end_sec = time_to_seconds(op_end)

#     for cmd in commands:
#         if cmd == "next":
#             new_pos = pos_sec + 10
#             if start_sec <= new_pos <= end_sec:
#                 pos_sec = new_pos
#             elif new_pos > end_sec:
#                 pos_sec = end_sec
#             else:
#                 pos_sec = min(new_pos, video_sec)
#         elif cmd == "prev":
#             new_pos = pos_sec - 10
#             if start_sec <= new_pos <= end_sec:
#                 pos_sec = new_pos
#             elif new_pos < start_sec:
#                 pos_sec = start_sec
#             else:
#                 pos_sec = max(new_pos, 0)

#     return seconds_to_time(pos_sec)


# 테스트 케이스들
test_cases = [
    ("34:33", "13:00", "00:55", "02:55", ["next", "prev"], "13:00"),
    ("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"], "06:55"),
    ("07:22", "04:05", "00:15", "04:07", ["next"], "04:17"),
]

for i, (video_len, pos, op_start, op_end, commands, expected) in enumerate(test_cases, 1):
    result = solution(video_len, pos, op_start, op_end, commands)
    print(f"Test Case {i}: Result = {result}, Expected = {expected}, {'PASS' if result == expected else 'FAIL'}")
