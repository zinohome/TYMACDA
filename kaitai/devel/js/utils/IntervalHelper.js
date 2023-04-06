define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    class IntervalHandler {
        constructor(sortedItems = []) {
            this.sortedItems = sortedItems;
        }
        indexOf(intervalStart) {
            var arr = this.sortedItems;
            var low = 0;
            var high = arr.length - 1;
            while (low <= high) {
                var testIdx = (high + low) >> 1;
                var testValue = arr[testIdx].end;
                if (intervalStart > testValue) {
                    low = testIdx + 1;
                }
                else if (intervalStart < testValue) {
                    high = testIdx - 1;
                }
                else {
                    return testIdx;
                }
            }
            return -low - 1;
        }
        searchRange(start, end) {
            var arr = this.sortedItems;
            end = end || start;
            var startIdx = this.indexOf(start);
            if (startIdx < 0)
                startIdx = ~startIdx;
            var result = [];
            for (var index = startIdx; index < arr.length; index++) {
                var item = arr[index];
                if (start <= item.end && item.start <= end)
                    result.push(item);
                else
                    break;
            }
            return { idx: startIdx, items: result };
        }
        addSorted(items) {
            if (items.length === 0)
                return;
            var insertIdx = this.indexOf(items[0].start);
            if (insertIdx < 0)
                insertIdx = ~insertIdx;
            this.sortedItems = this.sortedItems.slice(0, insertIdx).concat(items, this.sortedItems.slice(insertIdx));
        }
    }
    exports.IntervalHandler = IntervalHandler;
});
