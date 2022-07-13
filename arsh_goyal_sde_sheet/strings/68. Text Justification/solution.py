class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_last_line():
            return " ".join(cur_line)  + (" " * (maxWidth - cur_size - len(cur_line) + 1))
        
        def get_line(cur_size, cur_line):
            space_left = maxWidth - cur_size
            space_between = len(cur_line) - 1
            if space_between == 0:
                return  cur_line[0] + (" " * space_left)
            rem = space_left % space_between
            line = ""
            index = 0
            space = " " * (space_left // space_between)
            while rem:
                line += cur_line[index] + space + " "
                rem -= 1
                index += 1
            line += space.join(cur_line[index:])
            return line
            
        paragraph = []
        cur_line = []
        cur_size = 0
        
        for word in words:
            space_between = len(cur_line) - 1
            filled = cur_size + space_between
            if filled == maxWidth:
                paragraph.append(" ".join(cur_line))
                cur_line = [word]
                cur_size = len(word)
                
            elif filled + len(word) + 1 > maxWidth:
                line = get_line(cur_size, cur_line)
                paragraph.append(line)
                cur_line = [word]
                cur_size = len(word)
                
            else:
                cur_line.append(word)
                cur_size += len(word)
        
        paragraph.append(get_last_line())
        return paragraph
                
                