class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def is_segmentable(s, word_dict):
            for word in word_dict:
                if word in s:
                    rs = [ w for w in s.split(word) if w.strip()]
                    if len(rs) == 0:
                        return True
                    
                    allrp_segmentable = True
                    for w in rs:
                        if not is_segmentable(w, word_dict):
                            allrp_segmentable = False
                            break
                    
                    if allrp_segmentable:
                        return True
            return False
        return is_segmentable(s, wordDict)
        
        