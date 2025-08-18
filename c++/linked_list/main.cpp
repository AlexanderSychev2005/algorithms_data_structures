#include <iostream>

using namespace std;

class Node {
public:
    double data;
    Node* next;

    Node(double data, Node* next = nullptr) : data(data), next(next) {}
// public:
//     Node(double data) {
//         this->data = data;
//         this->next = nullptr;
//     }
};
class OneLinkedList {
public:
    Node* head, * tail;

    OneLinkedList(Node* head = nullptr, Node* tail = nullptr): head(nullptr), tail(nullptr) {}
    ~OneLinkedList() {
        while (head != nullptr) pop_front();
    }

    void pop_front() {
        if (head == nullptr) return;
        if (head == tail) {
            delete tail;
            head = tail = nullptr;
            return;
        }
        Node* node = head;
        head = head->next;
        delete node;
    }

    void push_back(double data) {
        Node* node = new Node(data);
        if (head == nullptr) head = node;
        if (tail != nullptr) tail->next = node;
        tail = node;
    }

    void push_front(double data) {
        Node* node = new Node(data);
        node->next = head;
        head = node;
        if (tail == nullptr) tail = node;
    }

    void pop_back() {
        if (tail == nullptr) return;
        if (head == tail) {
            delete tail;
            head = tail = nullptr;
            return;
        }
        Node* node = head;
        for (;node->next != tail; node = node->next);
        delete tail;
        node->next = nullptr;
        tail = node;
    }

    Node* getAt(int k) {
        if (k < 0) return nullptr;
        Node* node = head;
        int n =0;
        while (node && n != k && node->next != nullptr) {
            node = node->next;
            n++;
        }
        return (n == k) ? node : nullptr;
    }

    void insert(int k, double data) {
        Node* left = getAt(k);
        if (left == nullptr) return;

        Node* right = left->next;
        Node* node = new Node(data);

        left->next = node;
        node->next = right;
        if (right == nullptr) tail = node;
    }

    void erase(int k) {
        if (k < 0) return;
        if (k == 0) {
            pop_front();
            return;
        }

        Node* left = getAt(k-1);
        Node* node = left->next;

        if (node == nullptr) return;
        Node* right = node->next;

        left->next = right;
        if (node == tail) tail = left;
        delete node;
    };
};

int main() {
    // Forward list in std;
    OneLinkedList lst;
    lst.push_front(1);
    lst.push_back(2);

    Node* n = lst.getAt(0);
    double d = (n != nullptr) ? n->data : 0;
    cout << d << endl;


    cout << endl;
    lst.erase(1);
    lst.insert(0, 5);
    lst.insert(0, 2);

    for (Node* node = lst.head; node != nullptr; node = node->next) {
        cout << node->data <<  " ";
    }
    return 0;
}