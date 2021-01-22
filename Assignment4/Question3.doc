#Write a Python program to find the middle of a linked list

#Answer:::


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = new


    def display(self):
        if self.head == None:
            print("No nodes to display")
            return
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

    def delete(self):
        if self.head == None:
            print("No nodes to delete")
            return

        self.head = self.head.next

    def findMid(self):
        if self.head == None:
            print("Its Empty")
            return
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next

        mid = count//2
        temp = self.head
        for i in range(0,mid):
            temp = temp.next

        print(temp.data)



l1 = LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)

l1.findMid()