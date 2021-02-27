try:
    import speller3x.checker as sc
    from algorithms3x.sort import merge_sort
    from dt_structures3x.hashtable import * 
except:
    raise ImportWarning("Please intall the package: spell-checker")
class Finder():

    def __init__(self, language):
        """
        Available languages are:\n
        english\n
        german\n
        french\n
        spanish\n
        italian\n

        Please choose one of them and type in exactly what's shown above!
        """
        reference = sc.Checker(text="00", languageinp=language)
        reference.bucketize()
        self.reference = reference

    def find(self, target:str):
        iterators = self.reference.ht.nodes[self.reference.ht.hash(target)]
        res = []
        
        while iterators != None:
            if merge_sort(iterators.val) == merge_sort(target):
                res.append(iterators.val)
            iterators = iterators.pointer
        return res
        
