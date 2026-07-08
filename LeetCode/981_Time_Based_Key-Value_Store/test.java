import java.util.*;

class TimeMap {
    private static class TimeValue {
        String value;
        int timestamp;

        TimeValue(String value, int timestamp) {
            this.value = value;
            this.timestamp = timestamp;
        }
    }

    private Map<String, List<TimeValue>> map;

    public TimeMap() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new TimeValue(value, timestamp));
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        List<TimeValue> list = map.get(key);
        return binarySearch(list, timestamp);
    }

    private String binarySearch(List<TimeValue> list, int targetTime) {
        int left = 0;
        int right = list.size() - 1;
        String res = "";

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (list.get(mid).timestamp == targetTime) {
                return list.get(mid).value;
            }
            if (list.get(mid).timestamp < targetTime) {
                res = list.get(mid).value;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}