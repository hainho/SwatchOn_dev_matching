import math

def init(info):
    value_score_dict = {}
    language_list = ['cpp', 'java', 'python', '-']
    position_list = ['backend', 'frontend', '-']
    career_list = ['junior', 'senior', '-']
    soul_food_list = ['chicken', 'pizza', '-']

    for language in language_list:
        for position in position_list:
            for career in career_list:
                for soul_food in soul_food_list:
                    cur_key = language + position + career + soul_food
                    value_score_dict[cur_key] = []
    
    for cur_info in info:
        splitted_cur_info = cur_info.split()
        languages = [splitted_cur_info[0], '-']
        positions = [splitted_cur_info[1], '-']
        careers = [splitted_cur_info[2], '-']
        soul_foods = [splitted_cur_info[3], '-']
        cur_score = int(splitted_cur_info[4])
        
        for language in languages:
            for position in positions:
                for career in careers:
                    for soul_food in soul_foods:
                        cur_key = language + position + career + soul_food
                        value_score_dict[cur_key].append(cur_score)

    for language in language_list:
        for position in position_list:
            for career in career_list:
                for soul_food in soul_food_list:
                    cur_key = language + position + career + soul_food
                    if len(value_score_dict[cur_key]) > 1:
                        value_score_dict[cur_key].sort()
    return value_score_dict

def b_search(target_list, target_score):
    start = 0
    end = len(target_list) - 1
    mid = math.ceil((start + end) / 2)
    while start <= end:
        if target_list[mid] >= target_score:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.ceil((start + end) / 2)
    return len(target_list) - mid

def execute_query(value_score_dict, query):
    answer = []
    for cur_query in query:
        splitted_cur_query = cur_query.split(" and ")
        soul_food, score = splitted_cur_query[-1].split()
        cur_key = splitted_cur_query[0] + splitted_cur_query[1] + splitted_cur_query[2] + soul_food
        cur_score = int(score)
        answer.append(b_search(value_score_dict[cur_key], cur_score))
    return answer

def solution(info, query):
    value_score_dict = init(info)
    answer = execute_query(value_score_dict, query)
    return answer