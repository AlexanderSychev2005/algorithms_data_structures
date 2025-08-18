#include <iostream>

using namespace std;

class Node {
public:
    double data;
    Node* prev;
    Node* next;

    Node(double data): data(data), prev(nullptr), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;
    Node* tail;

    LinkedList(): head(nullptr), tail(nullptr) {}
    ~LinkedList() {
        while (head != nullptr) {
            pop_front();
        }
    }

    Node* push_front(double data) {
        Node* ptr = new Node(data);
        ptr->next = head;
        if (head != nullptr) {
            head->prev = ptr;
        }
        if (tail == nullptr) {
            tail = ptr;
        }
        head = ptr;

        return ptr;
    }

    Node* push_back(double data) {
        Node* ptr = new Node(data);
        ptr->prev = tail;
        if (tail != nullptr) {
            tail->next = ptr;
        }
        if (head == nullptr) {
            head = ptr;
        }
        tail = ptr;

        return ptr;
    }

    void pop_front() {
        if (head == nullptr) return;
        Node* ptr = head->next;
        if (ptr != nullptr) {
            ptr->prev = nullptr;
        }
        else
            tail = nullptr;

        delete head;
        head = ptr;
    }

    void pop_back() {
        if (tail == nullptr) return;
        Node* ptr = tail->prev;
        if (ptr != nullptr) {
            ptr->next = nullptr;
        }
        else
            head = nullptr;

        delete tail;
        tail = ptr;
    }

    Node* getAt(int k) {
        Node* ptr = head;
        int n = 0;
        while (n != k) {
            if (ptr == nullptr) return ptr;
            ptr = ptr->next;
            n++;
        }
        return ptr;
    }

    Node* operator[](int k) {
        return getAt(k);
    }

    Node* insert(int index, double data) {
        Node *right = getAt(index);
        if (right == nullptr) {
            return push_back(data);
        }
        Node* left = right->prev;
        if (left == nullptr) {
            return push_front(data);
        }

        Node* ptr = new Node(data);
        ptr->prev = left;
        ptr->next = right;

        left->next = ptr;
        right->prev = ptr;

        return ptr;
    }

    void erase(int index) {
        Node* ptr = getAt(index);
        if (ptr == nullptr) return;

        if (ptr->prev == nullptr) {
            pop_front();
            return;
        }
        if (ptr->next == nullptr) {
            pop_back();
            return;
        }

        Node* left = ptr->prev;
        Node* right = ptr->next;
        left->next = right;
        right->prev = left;

        delete ptr;
    }
};

int main() {
    LinkedList lst;
    lst.push_back(1.0);
    lst.push_back(2.0);
    lst.push_back(3.0);
    lst.push_back(5.0);

    for (Node* ptr = lst.head; ptr != nullptr; ptr = ptr->next) {
        cout << ptr->data << " ";
    }
    cout << endl;

    for (Node* ptr = lst.tail; ptr != nullptr; ptr = ptr->prev) {
        cout << ptr->data << " ";
    }
    cout << endl;

    lst.insert(3, 4.0);
    for (Node* ptr = lst.head; ptr != nullptr; ptr = ptr->next) {
        cout << ptr->data << " ";
    }
    cout << endl;

    cout << lst[3]->data << endl;

    lst.insert(2, -5);
    lst.insert(20, -10);
    lst.erase(3);
    lst.erase(20);

    for (Node* ptr = lst.head; ptr != nullptr; ptr = ptr->next) {
        cout << ptr->data << " ";
    }
    cout << endl;
}

