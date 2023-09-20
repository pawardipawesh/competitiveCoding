class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def is_segmentable(s, word_dict):
            # iss_l = []
            for word in word_dict:
                if word in s:
                    rs = [ w for w in s.split(word) if w.strip()]
                    if len(rs) == 0:
                        # print('rs: ', rs)
                        return True
                    
                    issp_l = []
                    for w in rs:
                        is_sp = is_segmentable(w, word_dict)
                        issp_l.append(is_sp)
                    
                    # iss_l.append(all(issp_l))
                    if all(issp_l):
                        return True
            return False
            # return any(iss_l)
        return is_segmentable(s, wordDict)
        
        