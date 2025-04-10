class Solution(object):
    def maximumBeauty(self, items, queries):
        # Step 1: Sort items by price
        items.sort()

        # Step 2: Sort queries while keeping track of their original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [0] * len(queries)
        max_beauty = 0
        i = 0  # Pointer for items

        # Step 3: Process each query
        for q, idx in sorted_queries:
            # Move pointer while price <= query
            while i < len(items) and items[i][0] <= q:
                max_beauty = max(max_beauty, items[i][1])
                i += 1
            result[idx] = max_beauty

        return result

#By Coding Moves
