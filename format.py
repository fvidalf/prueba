def fill_gaps(string, reqr):
    if len(string) < reqr:
        string = "0" * (reqr - len(string)) + string
    return string

def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int(elapsed_time // 60 - (hours * 60))
    seconds = int(elapsed_time - (minutes * 60 + hours * 3600))
    miliseconds = round(elapsed_time % 1 * 1000)
    formatted_time = str(hours) + ":" + fill_gaps(str(minutes), 2) + ":" + fill_gaps(str(seconds), 2) + ":" + fill_gaps(str(miliseconds), 3)
    return formatted_time

def matrix_form_lines(data, split_chr):
    matrix = []
    for cs in data:
        matrix.append(cs.strip().split(split_chr))
    return matrix
