import datetime

class Asset:
    def __init__(self, name, id_num):
        self.name = name
        self._id = id_num
        self.checked_out = False

    def get_id(self):
        return self._id

    def print_details(self):
        status = "Out" if self.checked_out else "Available"
        return "[ID: " + str(self._id) + "] " + self.name + " (" + status + ")"


class Book(Asset):
    def __init__(self, name, id_num, author, pages):
        super().__init__(name, id_num)
        self.author = author
        self.pages = int(pages)

    def print_details(self):
        status = "Out" if self.checked_out else "In"
        return f"Book: {self.name} by {self.author} [{self._id}] - Status: {status}"


class SystemManager:
    def __init__(self):
        self.books = []

    def load_item(self, obj):
        self.books.append(obj)
        print(f"Added item: {obj.name}")

    def view_all(self):
        if len(self.books) == 0:
            print("Database empty")
            return
        print("Listing all inventory items:")
        for b in self.books:
            print(b.print_details())

    def rent_out(self, target_id):
        found = False
        for b in self.books:
            if b.get_id() == target_id:
                found = True
                if b.checked_out:
                    print(f"Fail: {b.name} is currently rented")
                else:
                    b.checked_out = True
                    print(f"Success: Rented {b.name}")
                break
        
        if not found:
            print("ID lookup failed")

    def return_back(self, target_id):
        found = False
        for b in self.books:
            if b.get_id() == target_id:
                found = True
                if not b.checked_out:
                    print(f"Fail: {b.name} was not out")
                else:
                    b.checked_out = False
                    print(f"Success: Returned {b.name}")
                break
        
        if not found:
            print("ID lookup failed")


if __name__ == '__main__':
    lib = SystemManager()

    b1 = Book("The Hobbit", "101", "Tolkien", 310)
    b2 = Book("1984", "102", "Orwell", 328)

    lib.load_item(b1)
    lib.load_item(b2)
    
    lib.view_all()

    lib.rent_out("101")
    lib.rent_out("101")
    
    lib.view_all()

    lib.return_back("101")
    lib.view_all()
