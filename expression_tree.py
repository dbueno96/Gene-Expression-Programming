import numbers

class TreeNode(): 
    
    def __init__(self, config, parent,function, arity, terminal= False,  children=None, str_rep=None): 
        # self.name =name
        self.conf=config
        self.parent= parent
        self.function= function
        self.arity= arity
        self.terminal = terminal
        self.children=[]
        self.depth= 0
        self.str_rep= str_rep
        if children is not None: 
            for child in children: 
                self.add_child(child) 
        if isinstance(function, numbers.Number): 
            self.terminal=True

        self.set_depth()
    
    def set_leaf_value(self,val):
        self.function=val

    def set_depth(self): 
        if self.parent is not None: 
            self.depth= 1+ self.parent.depth

    def add_child(self, child): 
        self.children.append(child)

    #Método encargado de construir el árbol de expresión a partir del nodo raíz. 
    #Se toman la operaciones de la variable OPERATOR, de acuerdo a los índices en el parámetro head.
    #se toman los nodos terminales del parámetro observation, de acuerdo a los índices del parámetro tail.
    def create_expression_tree(self, head, tail, observation):
        
        stack = []#Se define el stack, donde se agregan los nodos que están en el árbol y que falta por agregar hijos.
        stack.append(self)
        count = 1
        while(len(stack) > 0): 
            node = stack[0]  #Se selecciona el primer elemento del stack
            stack= stack[1:] #Se elimina del stack
            for i in range(node.arity): ##FOR encargado de crear los hijos de cada nodo, de acuerdo a la aridad de la operación que representa el ndoo
                if count < self.conf.head_size-1:   #IF encargado de crear un nodo con el padre tomado del stack y la información de la cabeza del cromosoma.
                    child_node = TreeNode(self.conf, node, self.conf.operators[head[0]][0], self.conf.operators[head[0]][1], str_rep= self.conf.operators[head[0]][2])
                    head = head[1:] #Se elimina la operación incluida en el árbol.
                    node.add_child(child_node) #Se registran los nuevos hijos del nodo
                    stack.append(child_node) #Se agregan los hijos al stack, para crear los hijos de estos posteriormente
                    count+=1
                else: ##ELSE ejecutado cuando ya no se crean los nodos con la inforación de la cabeza, sino del cola del cromosoma (terminales)
                    terminal_node = TreeNode(self.conf, node, observation[tail[0]], 0, terminal= True, str_rep=str(observation[tail[0]]))
                    tail= tail[1:] #Se elimina el índice ya usado
                    node.add_child(terminal_node)  #Se registra el nuevo nodo términal
                    count+=1
            
            if node.arity == 0: ##Caso especial para el operador LITERAL, que tiene aridad 0
                terminal_node = TreeNode(self.conf, node, observation[tail[0]], 0, terminal= True, str_rep=str (observation[tail[0]]))
                tail= tail[1:] #se elimina el índice ya usado.
                node.add_child(terminal_node) #Se registra el nuevo nodo terminal,.
                count+=1
            

    #Se evalúa el árbol de expresión por medio de recursión. 
    #El caso el base es cuando se llega a un nodo terminal, retornando el valor del nodo.
    #Los casos recursivos se dan de acuerdo a aridad de la operación, o la cantidad de hijos del nodo. 
    #Para estos casos se retorna la operación del nodo, y pasa como argumentos el llamado al método por parte de los hijos.
    def evaluate_tree(self): 
        if self.terminal: 
            return self.function
        elif self.arity==0: 
            return self.function(self.children[0].evaluate_tree() )
        elif self.arity==1: 
            return self.function(self.children[0].evaluate_tree() )
        elif self.arity==2: 
            return self.function(self.children[0].evaluate_tree(), 
                                self.children[1].evaluate_tree())
        elif self.arity==3:
            return self.function(self.children[0].evaluate_tree(), 
                                self.children[1].evaluate_tree(),
                                self.children[2].evaluate_tree())
        elif self.arity==4:
            return self.function(self.children[0].evaluate_tree(), 
                                self.children[1].evaluate_tree(),
                                self.children[2].evaluate_tree(),
                                self.children[3].evaluate_tree())
        else: 
            return 0