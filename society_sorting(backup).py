import numpy as np
import matplotlib.pyplot as plt

class People:
    def __init__(self, x_people_amount, y_people_amount, attributes_amount=10, party_amount=2, max_attribute_value=10):
        self.people_x=x_people_amount
        self.people_y=y_people_amount
        self.attributes_amount=attributes_amount
        self.max_attribute_value=max_attribute_value
        self.party_amount=party_amount
        self.attributes=[]
        self.party=np.array([])
        self.party_symbols=[".", "+"]
        self.create_people_behavior(self.attributes_amount, self.party_amount)
        self.figures=[]
        # self.sub=[]
        
    
    def survey(self):
        print("total amount of people: %d" % (self.people_x*self.people_y))
        x_axis=np.array([list(range(0, self.people_x)) for y in range(0, self.people_y)])
        y_axis=np.array([[y for x in range(0, self.people_x)] for y in range(0, self.people_y)])
        # self.sub.append(self.figure.add_subplot(1, len(self.sub)+1, len(self.sub)+1))
        fig=plt.figure()
        self.figures.append(fig)
        ax=fig.add_subplot()

        for i in range(0, self.party_amount):
            masked_x=np.ma.masked_where(self.party==i, x_axis)
            masked_y=np.ma.masked_where(self.party==i, y_axis)
            ax.scatter(masked_x, masked_y, c=self.attributes[0] ,s=120 ,cmap="Set1" , marker=self.party_symbols[i])
        
    
    def reset(self):
        self.create_people_behavior(self.attributes_amount, self.party_amount)


    def create_people_behavior(self, dynamics_Attribute_amount, static_Attribute_amount):
        for _ in range(0, dynamics_Attribute_amount):
            self.attributes.append(np.random.randint(0, self.max_attribute_value, (self.people_x, self.people_y)))
        self.party=np.random.randint(0, static_Attribute_amount, (self.people_x, self.people_y))

    def add_symbol(self, sym) -> None:
        self.party_symbols.append(sym)
        print("current symbols: {}".format(self.party_symbols))

    # def convert_symbol(self, num):
    #     symbol_covertor=np.frompyfunc(self.select_symbol, 1, 1)
    #     return symbol_covertor(num)

    # def select_symbol(self, num):
    #     if (num==0):
    #         return "."
    #     if (num==1):
    #         return "+"
    #     if (num==2):
    #         return "*"

class Society:
    def __init__(self, people: People):
        self.people_in_society=people
        self.neighborhood=np.array([(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x!=0 or y!=0)])
        self.global_agent=8
        self.c=4 #partisan effect
        self.homophily=8
        self.agent=self.select_agent()
    
    def evolve(self):
        self.agent=self.select_agent()
        neighbors=self.select_neighbor()
        similarities=self.weighting(neighbors)
        if (np.sum(similarities)==1):
            reference_neighbor=np.random.default_rng().choice(neighbors, p=similarities)
            
            attributes_list_of_neighbor=[]
            for attibute in self.people_in_society.attributes:
                attributes_list_of_neighbor.append(attibute[reference_neighbor[0], reference_neighbor[1]])
            # print(f"neighbor's attributes:{np.array(attributes_list_of_neighbor)}")
            for i in range(0, len(attributes_list_of_neighbor)):
                # print(self.people_in_society.attributes[i][self.agent[0]][self.agent[1]], end=", ")
                self.people_in_society.attributes[i][self.agent[0], self.agent[1]]=attributes_list_of_neighbor[i]
                # print(self.people_in_society.attributes[i][self.agent[0]][self.agent[1]], end=", ")
        else: print("skipping because of no similar neighbor!")
        
    
    def weighting(self, neighbors) -> np.array:
        similarity_list=[]
        print("similarities of neighbors:")
        for neighbor in neighbors:
            similarity_list.append(self.similarity(self.agent, neighbor))
            print(self.similarity(self.agent, neighbor))
        
        similarity_list=np.array(similarity_list)
        if (np.sum(similarity_list**self.homophily)!=0):
            similarity_list=(similarity_list**self.homophily)/np.sum(similarity_list**self.homophily)
        
        # print(f"current agent position: {self.agent}")
        # print(np.sum(similarity_list**self.homophily))
        print(f"weights of the neighborhood: {similarity_list}")

        return similarity_list

    def select_neighbor(self) -> list:
        local_neighbors=[]
        for neighbor in self.neighborhood:
            correct_neighbor_position=self.index_circulating(self.agent+neighbor)
            local_neighbors.append(correct_neighbor_position)
        # print(f"local neighbors: {np.array(local_neighbors)}")

        choice=np.random.choice(len(local_neighbors), size=self.global_agent, replace=False)
        global_neighbors=local_neighbors
        for i in range(0, len(choice)):
            global_agent_index=np.array([np.random.randint(self.people_in_society.people_y), np.random.randint(self.people_in_society.people_x)])
            global_neighbors[choice[i]]=global_agent_index
        # print(f"global neighbors: {np.array(global_neighbors)}")

        return global_neighbors

    def similarity(self, agent_location, otherone_location) -> float:
        delta=0
        for attribute in self.people_in_society.attributes:
            if (attribute[agent_location[1]][agent_location[0]]==attribute[otherone_location[1]][otherone_location[0]]):
                delta=delta+1
        
        if (self.people_in_society.party[agent_location[1]][agent_location[0]]==self.people_in_society.party[otherone_location[1]][otherone_location[0]]):
            delta=delta+1
        
        return delta/(self.c+self.people_in_society.attributes_amount)
    
    def index_circulating(self, index: list):
        for i in range(0, len(index)):
            index[0]=index[0] % self.people_in_society.people_y
            index[1]=index[1] % self.people_in_society.people_x
        return index

    def select_agent(self):
        return np.array([np.random.randint(self.people_in_society.people_x), np.random.randint(self.people_in_society.people_y)])

    def set_party_influence(self, party_influence):
        self.c=party_influence

    def set_global_agent_number(self, num):
        self.global_agent=num

    def set_homophily(self, h):
        self.homophily=h

    def info(self):
        print(f"global agent number: {self.global_agent}")
        print(f"homophily: {self.homophily}")
        print(f"partisan influence: {self.c}")
        print(f"total amount of people: {self.people_in_society.people_x*self.people_in_society.people_y}")
    
    def record(self):
        self.people_in_society.survey()
        print(self.people_in_society.figures)







p=People(30, 30)
s=Society(p)
# s.report()
s.record()
for i in range(0, 5000):
    print(f"steps: {i}")
    s.evolve()
s.record()
plt.show()


# print(s.similarity((0, 0), (0, 1)))
# s.weighting()
# s.select_neighbor()
# print(s.neighborhood)
# print(np.sum(s.weighting()))
# p.report()

# p.add_symbol("*")
# p.report()


# x=np.array([list(range(0, s.people_x)) for y in range(0, s.people_y)])
# y=np.array([[y for x in range(0, s.people_x)] for y in range(0, s.people_y)])
# masked_x=np.ma.masked_where(s.party==0, x)
# masked_y=np.ma.masked_where(s.party==0, y)
# plt.scatter(masked_x, masked_y, c="black", marker=".")
# masked_x=np.ma.masked_where(s.party==1, x)
# masked_y=np.ma.masked_where(s.party==1, y)
# plt.scatter(masked_x, masked_y, c="black", marker="+")
# plt.show()
