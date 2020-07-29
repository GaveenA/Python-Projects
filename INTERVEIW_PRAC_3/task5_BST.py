class SearchTreeNode:
    """
    Obtained from Week 11 Lectures

    """

    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.children = [left, right]
        self.deleted = False

    def __str__(self):
        """
        Returns string representation of the node.

        @:return: String representation
        @pre-condition: none
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)
        """
        return str("Node with item " + str(self.item))

    def get_child_for_key(self, key):
        return self.children[int(key > self.key)]

    def set_child_for_key(self, key, child):
        self.children[int(key > self.key)] = child


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, item):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        self.root = self._setitem_aux(self.root, key, item)

    def _setitem_aux(self, node, key, item):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        if node is None:
            node = SearchTreeNode(key, item)
        else:
            if node.key == key:
                # we replace
                node.item = item
            else:
                node.set_child_for_key(key,
                                       self._setitem_aux(node.get_child_for_key(key), key, item))
        return node

    def __getitem__(self, key):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        return self._getitem_aux(self.root, key)

    def _getitem_aux(self, node, key):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        if node is None or node.deleted is True:
            raise KeyError("key not found")
        if key == node.key:
            return node.item
        else:
            return self._getitem_aux(node.get_child_for_key(key), key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __delitem__(self, key):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        """We only implement a lazy deletion.
           See slides for "classic" deletion."""
        self._delitem_aux(self.root, key)

    def _delitem_aux(self, node, key):
        """
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(n)

        """
        if node is None:
            raise KeyError("key not found")
        if key == node.key:
            node.deleted = True
        else:
            self._delitem_aux(node.get_child_for_key(key), key)



