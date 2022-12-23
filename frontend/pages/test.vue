<template>
    <!-- <Login/> -->
    <div class="container">
        <ul>
            <li v-for="(item, index) in data" :key="index">
                {{ fmDate(item.start) }} - {{ fmDate(item.end) }}
            </li>
        </ul>
    </div>
</template>
<script>
import { format as formatDate, parse, addSeconds, subSeconds } from "date-fns";
const reservations = [
    {
        id: 1,
        start: parse("2022-12-06 08:00", "yyyy-MM-dd HH:mm", new Date()),
        end: parse("2022-12-06 09:30", "yyyy-MM-dd HH:mm", new Date()),
    },
    {
        id: 2,
        start: parse("2022-12-06 11:00", "yyyy-MM-dd HH:mm", new Date()),
        end: parse("2022-12-06 14:00", "yyyy-MM-dd HH:mm", new Date()),
    },
];
const submitStart = parse("2022-12-06 09:30", "yyyy-MM-dd HH:mm", new Date());
const submitEnd = parse("2022-12-06 11:00", "yyyy-MM-dd HH:mm", new Date());
const containDates = (
    list = [
        {
            id: NaN,
            start: new Date(),
            end: new Date(),
        },
    ],
    start = new Date(),
    end = new Date()
) => {
    const newStart = addSeconds(start, 1);
    const newEnd = subSeconds(end, 1);
    return list.filter((element) => {
        return (
            (newStart < element.start && element.start < newEnd) ||
            (newStart < element.end && element.end < newEnd) ||
            (element.start < newStart && newStart < element.end) ||
            (element.start < newEnd && newEnd < element.end)
        );
    });
};
const foundDates = containDates(reservations, submitStart, submitEnd);

export default {
    name: "Home",
    layout: "blank",
    auth: false,
    data() {
        return {
            data: foundDates,
        };
    },
    methods: {
        fmDate(date = new Date()) {
            return formatDate(date, "yyyy-MM-dd HH:mm");
        },
    },
};
</script>
