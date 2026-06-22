import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self.idMap={}
        pass

    def getAnni(self):
        return DAO.getAllYears()

    def getPiloti(self,a,b):
        return DAO.getPiloti(a,b)

    def getNumNodi(self):
        return len(self._grafo.nodes())


    def getNumArchi(self):
        return len(self._grafo.edges())


   # def getArchi(self,a,b,idMap):
   #     return DAO.getArchi(a,b,idMap)

    def buildGrafo(self,a,b):
        self._grafo.clear()

        for p in self.getPiloti(a,b):
            self._grafo.add_node(p)
            self.idMap[p.driverId]=p

        archi = DAO.getArchi(a,b,self.idMap)
        for arco in archi :
            self._grafo.add_edge(arco.pilota1,arco.pilota2,weight=arco.peso)


    def ArchiPeso3Maggiore(self):
        archi = sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight'],reverse=True)
        return archi[:3]

    def getNumCompConnessa(self):
        num_componenti =(nx.number_connected_components(self._grafo))
        return num_componenti

    def getMaggioreConnessa(self):
        comp_maggiore=max(nx.connected_components(self._grafo),key=len)
        num_nodi=len(comp_maggiore)
        return num_nodi,comp_maggiore










