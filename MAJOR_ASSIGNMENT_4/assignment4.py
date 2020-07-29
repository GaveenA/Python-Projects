class Vertex:
    """
    This class is used to represent the Vertex and its attributes
    This class holds an attribute edges, which represents the edges connected to a a particular vertex
    There is also a method add_edge to add an edge to the list of edges.
    """

    def __init__(self,id,word):
        """
        This method initilaizes the vertex by initializing the attributes for the vertex.
        :param id: The ID of the vertex
        :param word: The word in the vertex
        """


        self.id = id
        self.optPrev = None         # Stores VertexID of prev Vertex
        self.word = word            # Word stored in vertex
        self.distance = 0           # Represents fistance of vertex from source (used in bfs)
        # print(self.word)
        # adjacency list
        self.edges = []     # Stores edges (of type EDGE) that are attached to an instance of VERTEX.
        # additional stuff
        self.visited = False        # Boolean var if a vertex is visited
        self.discovered = False     # Boolean var if a vertex is discovered

    def add_edge(self, edge):
        """
        This method is used to append an edge to the list of edges for a particular vertex.
        :param edge:
        :return:
        """

        self.edges.append(edge)

class Edge:
    """
    This class is used to represent the edges and contains the attributes for each edge
    """

    def __init__(self, u, v, w=0):

        self.u = u      # Represents the staring vertex
        self.v = v      # Represents the end vertex
        self.w = w      # Represents the weight


class Graph:
    """
    This class represents the Graph and its methods and attributes.
    The graph is a simple undirected graph
    The graph is such that each vertex represents a word, and there is an edge between two vertices
    if and only if those two words differ by exactly one character.
    """

    def __init__(self,vertices_filename, edges_filename):
        """
        The attributes of the graph are initialized.
        The graph is given as two files, the first containing information about the vertices, and the second
        containing information about the edges.

        This function takes two file-names as inputs, and reads the data from them.
        The first line of vertices_filename has a number, n, which is the number of vertices in the graph.
        The next n lines each start with a unique integer between 0 and n − 1 inclusive (the vertex ID) and then a space, and then a word (the word which that vertex represents).
        The words will contain only lowercase English alphabet characters.
        We assume that all words are constant size.

        Each line of edges_filename consists of two numbers, separated by a a space.
        Each of these pairs of numbers represents an undirected edge connecting the two vertices with those IDs.
        You are guaranteed that all the numbers in edges_filename are valid vertex IDs (i.e. are integers between 0 and n − 1 inclusive).
        The edges are in no particular order.
        This innit mehtthod will correctly populate an instance of your Graph class, taking into consideration each vertice and all the
        vertices linked to that vertice via an edge.

        We go about populating the graph class by iterating over each line of the vertice file, and since the first line

        :param vertices_filename:
        :param edges_filename:
        """

        verticeFile = open(vertices_filename,'r')
        edgesFile = open(edges_filename,'r')

        lineIndex = 0   # Tracking the liens being read in vertices File

        for line in verticeFile:        # O(v) , v is number of lines in vertices File

            if (lineIndex == 0):    # The first line of the file contains the number of vertices in the graph
                n = int(line.split()[0])    # n represents the number if vertices
                self.numOfVertices = n
                if (n <= 0):
                    raise Exception("The value representing number of vertices (first line of vertices file) must be greater than 0")
                else:
                    self.vertexArray = [None]*n
                # print(n)
            else:
                tuple = line.split()    # Tuple has in its first element the vertex ID, and in its second element the word
                vertexID = int(tuple[0])
                self.vertexArray[vertexID] = Vertex(int(tuple[0]),tuple[1])    # Creating a vertex, storing ID and corresponding word
            lineIndex += 1

        for line in edgesFile:          # O(E)  where E is the number of lines in edges file

            id_pair = line.split()
            id_one = int(id_pair[0])
            id_two = int(id_pair[1])
            if id_one == self.vertexArray[int(id_pair[0])].id:
                edge = Edge(int(id_pair[0]),int(id_pair[1]))
                self.vertexArray[int(id_pair[0])].add_edge(edge)
            if id_two == self.vertexArray[int(id_pair[1])].id:
                edge = Edge(int(id_pair[1]),int(id_pair[0]))
                self.vertexArray[int(id_pair[1])].add_edge(edge)


        verticeFile.close()
        edgesFile.close()



    # TASK 2



    def solve_ladder(self, start_vertex, target_vertex):
        """
        function which finds the shortest list of intermediate words which solves it (or reports that no such list exists)
        start_vertex and target_vertex. These are integers between 0 and V − 1 inclusive, where V is the number of vertices in the graph.
        The function should return a list of strings, which correspond to the words in the word ladder from start_vertex to target_vertex. In some cases,
        it may not be possible to find a chain from the start_vertex to the target_vertex.
        In these cases, the function should return False.

        :param start_vertex:
        :param target_vertex:
        :return:
        """

        try:
            wordList = []
            discovered = Queue()
            self.bfs(discovered,self.vertexArray[start_vertex])
            self.findWords(self.vertexArray[target_vertex],start_vertex,wordList)
            return wordList
        except:
            return False


    def findWords(self,vertex,startID,list):
        """
        This function recurses over the vertex Array from vertex which is the end vertex, all the way to the
        start vertex.
        In this function we use the predecessor or optPrev vertex from the end vertex to make our way back to the start vertex by
        calling this function recursively providing the vertex.optPrev as the first param in each recursive call of the fucntion.
        At each recursive call we append the word of the 'vertex' into the list which is returned finally

        :param vertex: The vertex from which to backtrack to start vertex
        :param startID: THe vertex, at which the backtrack ends
        :param list: A list of words showing the path from start vertex to end vertex
        :return: none
        """


        if vertex.optPrev is None and vertex.id == startID:
            list.append(vertex.word)
            return
        elif (vertex.optPrev is None) and (not vertex.id == startID):
            raise Exception("No path found to Destination ")
        else:
            self.findWords(self.vertexArray[vertex.optPrev],startID,list)
            list.append(vertex.word)


    def bfs(self,discovered,source):
        """
        We then call the function bfs (breadth first search) providing the queue and start vertex as parameters.

        In the breadth first search function we start off by removing the first vertex object from the queue (vertex at the front of the queue) and set the ‘visited’
        attribute of the vertex as True, and we iterate over all the edges connected to that vertex.

        In an edge,
        if the “destination vertex” of that edge is not discovered nor visited {

        The destination vertex is added to the discovered Queue and the discovered attribute of the vertex is set to True.
        We also update the distance of that destination vertex based on a calculation considering the distance of the current visiting vertex (from source),
        and the predecessor of the destination vertex is set to the current visiting vertex [O(1)].

        If the “destination vertex” is already discovered {
        We calculate the “current distance” from the source vertex, by taking into consideration the distance of the current visiting vertex (from source).
        We then proceed to check if the “current distance” is less than the distance mentioned in the distance attribute of the “destination vertex”. If so,
        the distance attribute of the “destination vertex” is now updated with the “current distance” [O(1)].

        This process now continues for all the edges that the vertices in the discovered Queue have.
        The BFS function executes in O(V+E). Where E is the total number of edges in the graph, and V is the total number of vertices in the graph

        :param discovered: The Queue to which we append the vertices being discovered
        :param source:  The vertex to start the search from
        :return: Visted Vertex
        """
        visited = []
        source.distance = 0
        discovered.append(source)
        source.discovered = True

        while not discovered.is_empty():

            item = discovered.serve()
            visited.append(item.word)
            # print(item.word)
            self.vertexArray[item.id].visited = True

            for edge in self.vertexArray[item.id].edges:

                v = edge.v
                # print(v)
                # self.vertexArray[v].distance = self.vertexArray[item.id].distance + 1
                newDist = self.vertexArray[item.id].distance + 1
                if newDist < self.vertexArray[v].distance and (self.vertexArray[v].discovered):
                    self.vertexArray[v].distance = newDist
                    self.vertexArray[v].optPrev = item.id
                elif (not self.vertexArray[v].discovered):
                    self.vertexArray[v].distance = self.vertexArray[item.id].distance + 1
                    self.vertexArray[v].optPrev = item.id

                # print(self.vertexArray[v].distance)
                if (not self.vertexArray[v].discovered) and (not self.vertexArray[v].visited):
                    discovered.append(self.vertexArray[v])
                    self.vertexArray[v].discovered = True
        return visited


    def costCal(self,presentCost, currentVertex, nextVertex):
        cost  = presentCost
        for i in range(len(currentVertex.word)):
            if currentVertex.word[i] == nextVertex.word[i]:
                pass
            else:
                cost += (ord(currentVertex.word[i])-ord(nextVertex.word[i]))**2
        return cost


    def dijkstra(self, startVertex, seekChar):
        """

        Dijkstra's algorithm is an algorithm we can use to find shortest distances or minimum costs depending on what is represented in a graph.
        You're basically working backwards from the end to the beginning, finding the shortest leg each time.
        In this algorithm we create a MinHeap and execute a loop which iterates while the heap is not empty.
        The dijstra algorithm works by finiding the chapest path to all the vertextes from the start vertex.

        :param startVertex:
        :param seekChar:
        :return:
        """

        pointer = False
        desiredCharFound = False

        cost_list = [None]*self.numOfVertices
        for i in range(self.numOfVertices):
            cost_list[i] = [float("inf"), i+1]

        cost_list[startVertex][0] = 0

        priorityQueue = MinHeap(cost_list)

        while(len(priorityQueue.heap_array)>1):
            heapTopData = priorityQueue.remove()
            currentVertexIndex = heapTopData[1] - 1
            currentVertex = self.vertexArray[currentVertexIndex]

            if currentVertex.word[0] == seekChar and desiredCharFound == False:
                desiredCharFound = True
                pointer = currentVertexIndex
            for edge in currentVertex.edges:
                v = edge.v
                nextVertex = self.vertexArray[v]
                presentCost = cost_list[currentVertexIndex][0]
                if self.costCal(presentCost,currentVertex,nextVertex) < cost_list[nextVertex.id][0]:
                    cost_list[nextVertex.id][0] = self.costCal(presentCost,currentVertex,nextVertex)
                    verticesPos = priorityQueue.returnVerticesList()
                    index = verticesPos[nextVertex.id+1]
                    priorityQueue.heap_array[index][0] = cost_list[nextVertex.id][0]
                    priorityQueue.floatUp(index)
                    nextVertex.optPrev = currentVertexIndex
        return cost_list,pointer


    def findWords2(self,vertex,startID,list):
        """
        This function recurses over the vertex Array from vertex which is the end vertex, all the way to the
        start vertex.
        In this function we use the predecessor or optPrev vertex from the end vertex to make our way back to the start vertex by
        calling this function recursively providing the vertex.optPrev as the first param in each recursive call of the fucntion.
        At each recursive call we append the word of the 'vertex' into the list which is returned finally

        :param vertex: The vertex from which to backtrack to start vertex
        :param startID: THe vertex, at which the backtrack ends
        :param list: A list of words showing the path from start vertex to end vertex
        :return: None

        """

        if vertex.optPrev is None and vertex.id == startID:
            list.append(vertex.word)
            return
        elif (vertex.optPrev is None) and (not vertex.id == startID):
            raise Exception("No path found to Destination")
        else:
            list.append(vertex.word)
            self.findWords2(self.vertexArray[vertex.optPrev],startID,list)


    def cheapest_ladder(self, startVertexIndex, targetVertexIndex, reqChar):
        """
        In the chapest_ladder function, we call dijkstras Algorithm once giving the start index as startVertexIndex.
        This initial call of Dijkstras [O(ElogV)] returns the ‘pointer’ variable containing the vertex ID of the first
        Vertex we come across with the char as the first name of vertex.word, this is also the cheapest vertex with char in word (as first character).

        We then make a call to findWords2(self, vertex, startVertexID,list) giving the ‘vertex’ param as vertexArray[pointer] and the second param as startVertex
        which in this instance the source vertex of the graph as determined by user.
        This function will then essentially backtrack using recursion and find the path from the pointer to the start vertex, by using the predecessor of the ‘vertex’ at each recursive call.
        Prior to each recrursive call we append the vertex.word to the ‘list’ which is returned after the final recursive call.
        We now have the cheapest path from the start vertex to the ‘pointer’ (first vertex we come across in Dijkstras with char as first character of word).

        We now run a second Dijkstras algorithm giving the startVertex as the ‘pointer’ (vertex ID of cheapest vertex with char as the first character of word) we obtained from the first
        Dijkstra call.
        This second Dijkstra call all of the cheapest paths from the cheapest vertex with char (as first character of word) to all other vertices in the connected grapgh.
        Afterward we make another call to findWords2(self, vertex, startVertexID, list) giving the ‘vertex’ param as vertexArray[targetVertexIndex] and the startVertexID as the ‘pointer’ returned
        from the first execution of Dijkstra.

        This function will then essentially backtrack using recursion and find the path from the pointer to the start vertex (pointer), by using the predecessor of the ‘vertex’ at each
        recursive call. Prior to each recrursive call we append the vertex.word to the ‘list’ which is returned after the final recursive call. We now have the cheapest path from the ‘pointer’
        to the  targetVertex (final target vertex as specified by the user in second param of cheapest_ladder func).

        We now combine the 2 paths and we get the full path from the startVertex to targetVertex, containing the cheapest vertex containing ‘char’ as its first character of the vertex.word
        (if such a vertex exists).

        This whole cheapest_ladder function excutes in O(E log(V )) time, where
        V is the number of vertices in the graph
        E is the number of edges in the graph

        :param startVertexIndex: The vertex to start the path from
        :param targetVertexIndex: Vertex at which path should end with the path containing the cheapest vertex with char in word (as first character)
        :param reqChar: The desired character  we are seeking
        :return: The final String or False
        """

        cost_firstIter, pointer1 = self.dijkstra(startVertexIndex, reqChar)

        if self.vertexArray[targetVertexIndex].optPrev == None:
            return False

        if pointer1 == False:
            return False

        word_path_1 = []

        currentVertex = self.vertexArray[pointer1]
        cost = cost_firstIter[pointer1][0]
        self.findWords2(currentVertex,startVertexIndex,word_path_1)
        word_path_1=word_path_1[::-1]


        word_path_2 = []

        cost_secondIter, pointer2 = self.dijkstra(pointer1, reqChar)

        # print(cost_secondIter)
        # for vertex in self.vertexArray:
        #     print(f"Vertex ID: {vertex.id} ; Pred: {vertex.optPrev}")


        self.vertexArray[pointer1].optPrev = None
        targetVertex = self.vertexArray[targetVertexIndex]
        self.findWords2(targetVertex, pointer1, word_path_2)
        cost += cost_secondIter[targetVertexIndex][0]


        word_path_2 = word_path_2[::-1]
        word_path_2 = word_path_2[1:]

        word_path_final = word_path_1+word_path_2

        finalString = cost,word_path_final

        return finalString

















class Queue:

    def __init__(self):
        """Builds a queue with given capacity > 0."""
        # if capacity <= 0:
        #     raise Exception("The capacity must be positive")
        self.the_array = []
        self.front = 0
        self.rear = 0

    def size(self):
        """Returns the size, i.e. the number
        of elements in the container."""
        return self.rear - self.front

    def is_empty(self):
        """Returns True if and only if the container is empty."""
        return self.size() == 0

    def append(self, item):
        """Places the given item at the end of the queue
        if there is capacity, or raises an Exception."""
        self.the_array.append(item)
        self.rear += 1

    def serve(self):
        """Removes and returns the first element of the queue,
        or raises an Exception if there is none."""
        if self.is_empty():
            raise Exception("The queue is empty")
        item = self.the_array[self.front]
        self.the_array[self.front] = None
        self.front += 1
        return item





class MinHeap:
    """
    This is the implementation of MinHeap, coded with aid from content learned in FIT2085
    """

    def __init__(self, items=[]):
        self.heap_array = [404]   # Initializing first elem of heap array as 404, as the heap indexes will start from 1
        self.vertice_index_list = [None]
        for item in items:
            self.insert(item)

    def floatUp(self, index):
        """
        Floating up the vertex after  being added to the bottom of the heap, if certain conditions are met
        :param index: The index of the heap Array to float upward from
        :return: None
        """
        parent = index // 2
        if index <= 1:
            return
        elif self.heap_array[index][0] < self.heap_array[parent][0]:
            swapIndex1 = self.heap_array[parent][1]
            swapIndex2 = self.heap_array[index][1]

            self.vertice_index_list[swapIndex1], self.vertice_index_list[swapIndex2] = self.vertice_index_list[swapIndex2], self.vertice_index_list[swapIndex1]
            self.swap(index, parent)
            self.floatUp(parent)

    def floatDown(self, index):
        """
        To remove an index the vertex at the top of the heap Array (min elem) is swapped with the
        vertex at the bottom of the heap array. float down is then called to move the index at the top back down the
        heap, if certain conditions are met, as detailed below in code.
        :param index: The index from which to begin the float down process
        :return: None
        """
        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap_array) > left and self.heap_array[smallest][0] > self.heap_array[left][0]:
            smallest = left
        if len(self.heap_array) > right and self.heap_array[smallest][0] > self.heap_array[right][0]:
            smallest = right
        if smallest != index:
            indexSwap1 = self.heap_array[smallest][1]
            indexSwap2 = self.heap_array[index][1]
            self.vertice_index_list[indexSwap1], self.vertice_index_list[indexSwap2] = self.vertice_index_list[indexSwap2], self.vertice_index_list[indexSwap1]
            self.swap(index, smallest)
            self.floatDown(smallest)

    def insert(self, data):
        """
        This function is used to add vertex Data to the minHeap. The data is a list containing the cost in the first elem
        of the list and the index of thw vertex in the vertexArray as the second elem.
        This 'data' is then appended to the end of the heap Array and float up funcntion is called.
        :param data: The vertex data added to the MinQueue, this is a list format with 2 elements
        :return: None
        """
        self.heap_array.append(data)
        self.vertice_index_list.append(len(self.heap_array) - 1)
        self.floatUp(len(self.heap_array) - 1)

    def remove(self):
        """
        This function is used to remove the minimum elem of the queue, which is the top most element (with index 1 ) of the heap_array
        This element is removed by swapping the top-most (index 1) elem of the heap array with the last element (index = len(heap array)-1 ) and removing the
        last elem of the heap-array.
        method float down is now called on the index 1 elem of the heap array to float the element downn the heap if certain conditions are met.

        :return: min or False
        """
        if len(self.heap_array) > 2:

            indexSwap1 = self.heap_array[1][1]
            indexSwap2 = self.heap_array[len(self.heap_array) - 1][1]

            self.vertice_index_list[indexSwap1], self.vertice_index_list[indexSwap2] = self.vertice_index_list[indexSwap2], self.vertice_index_list[indexSwap1]
            self.swap(1, len(self.heap_array) - 1)

            min = self.heap_array.pop()
            self.vertice_index_list[min[1]] = "end"
            self.floatDown(1)

        elif len(self.heap_array) == 2:
            min = self.heap_array.pop(1)
            self.vertice_index_list[min[1]] = "end"
        else:
            min = False
        return min

    def swap(self, i, j):
        """
        Fucntion is used to swap different elements of the heap array, given 2 indexes i and j
        :param i: index of heap array elem to swap with
        :param j: index of heap array elem to swap with
        :return: None
        """
        self.heap_array[i], self.heap_array[j] = self.heap_array[j], self.heap_array[i]

    def returnVerticesList(self):
        """
        This function returns the vertice_index_list which tracks the index of each vertex in the heap, this is down because
        the index of the vertex in the heap changes dynamically after each insert and remove and float down and float up
        :return: vertice_index_list
        """
        return self.vertice_index_list




if __name__ == '__main__':

    my_graph = Graph('vertices.txt','edges.txt')
    # for vertex in my_graph.vertexArray:
    #     for edge in vertex.edges:
    #        print(f"Vertex ID: {vertex.id} ; Vertex Word: {vertex.word}  ; Vertex Edges: {edge.u,edge.v}")

    print("\nTask1:\n")
    print(my_graph.solve_ladder(0, 6))

    print("\n")

    print("\nTask2:\n")
    print(my_graph.cheapest_ladder(0,6,"c"))

