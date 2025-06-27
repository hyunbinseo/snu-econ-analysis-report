const holidayDates = [
	'2018-01-01',
	'2018-02-15',
	'2018-02-16',
	'2018-02-17',
	'2018-03-01',
	'2018-05-05',
	'2018-05-07',
	'2018-05-22',
	'2018-06-06',
	'2018-06-13',
	'2018-08-15',
	'2018-09-23',
	'2018-09-24',
	'2018-09-25',
	'2018-09-26',
	'2018-10-03',
	'2018-10-09',
	'2018-12-25',
	'2019-01-01',
	'2019-02-04',
	'2019-02-05',
	'2019-02-06',
	'2019-03-01',
	'2019-05-05',
	'2019-05-06',
	'2019-05-12',
	'2019-06-06',
	'2019-08-15',
	'2019-09-12',
	'2019-09-13',
	'2019-09-14',
	'2019-10-03',
	'2019-10-09',
	'2019-12-25',
	'2020-01-01',
	'2020-01-24',
	'2020-01-25',
	'2020-01-26',
	'2020-01-27',
	'2020-03-01',
	'2020-04-15',
	'2020-04-30',
	'2020-05-05',
	'2020-06-06',
	'2020-08-15',
	'2020-09-30',
	'2020-10-01',
	'2020-10-02',
	'2020-10-03',
	'2020-10-09',
	'2020-12-25',
	'2021-01-01',
	'2021-02-11',
	'2021-02-12',
	'2021-02-13',
	'2021-03-01',
	'2021-05-05',
	'2021-05-19',
	'2021-06-06',
	'2021-08-15',
	'2021-09-20',
	'2021-09-21',
	'2021-09-22',
	'2021-10-03',
	'2021-10-09',
	'2021-12-25',
	'2022-01-01',
	'2022-01-31',
	'2022-02-01',
	'2022-02-02',
	'2022-03-01',
	'2022-03-09',
	'2022-05-05',
	'2022-05-08',
	'2022-06-01',
	'2022-06-06',
	'2022-08-15',
	'2022-09-09',
	'2022-09-10',
	'2022-09-11',
	'2022-09-12',
	'2022-10-03',
	'2022-10-09',
	'2022-10-10',
	'2022-12-25',
	'2023-01-01',
	'2023-01-21',
	'2023-01-22',
	'2023-01-23',
	'2023-01-24',
	'2023-03-01',
	'2023-05-05',
	'2023-05-27',
	'2023-05-29',
	'2023-06-06',
	'2023-08-15',
	'2023-09-28',
	'2023-09-29',
	'2023-09-30',
	'2023-10-02',
	'2023-10-03',
	'2023-10-09',
	'2023-12-25',
	'2024-01-01',
	'2024-02-09',
	'2024-02-10',
	'2024-02-11',
	'2024-02-12',
	'2024-03-01',
	'2024-04-10',
	'2024-05-05',
	'2024-05-06',
	'2024-05-15',
	'2024-06-06',
	'2024-08-15',
	'2024-09-16',
	'2024-09-17',
	'2024-09-18',
	'2024-10-01',
	'2024-10-03',
	'2024-10-09',
	'2024-12-25',
];

const addDateDays = (dateStr: string, days: number): string => {
	const date = new Date(dateStr);
	date.setDate(date.getDate() + days);
	return date.toISOString().split('T')[0];
};

const isWeekend = (dateStr: string): boolean => {
	const date = new Date(dateStr);
	const dayOfWeek = date.getDay();
	return dayOfWeek === 0 || dayOfWeek === 6;
};

const extendHolidaysWithWeekends = (holidays: string[]): string[] => {
	const holidaySet = new Set(holidays);
	const extendedHolidays = new Set(holidays);

	holidays.forEach((holiday) => {
		let currentDate = holiday;

		while (true) {
			const prevDate = addDateDays(currentDate, -1);
			if (isWeekend(prevDate) || holidaySet.has(prevDate)) {
				extendedHolidays.add(prevDate);
				currentDate = prevDate;
			} else {
				break;
			}
		}

		currentDate = holiday;
		while (true) {
			const nextDate = addDateDays(currentDate, 1);
			if (isWeekend(nextDate) || holidaySet.has(nextDate)) {
				extendedHolidays.add(nextDate);
				currentDate = nextDate;
			} else {
				break;
			}
		}
	});

	const addSingleDayGaps = (dates: string[]): string[] => {
		const dateSet = new Set(dates);
		const result = new Set(dates);

		dates.forEach((date) => {
			const dayAfterTomorrow = addDateDays(date, 2);
			if (dateSet.has(dayAfterTomorrow)) {
				const gapDay = addDateDays(date, 1);
				if (!isWeekend(gapDay)) {
					result.add(gapDay);
				}
			}
		});

		return Array.from(result);
	};

	const firstExtension = Array.from(extendedHolidays);
	const withGaps = addSingleDayGaps(firstExtension);
	const finalExtended = new Set(withGaps);

	withGaps.forEach((date) => {
		let currentDate = date;

		while (true) {
			const prevDate = addDateDays(currentDate, -1);
			if (isWeekend(prevDate) || finalExtended.has(prevDate)) {
				finalExtended.add(prevDate);
				currentDate = prevDate;
			} else {
				break;
			}
		}

		currentDate = date;
		while (true) {
			const nextDate = addDateDays(currentDate, 1);
			if (isWeekend(nextDate) || finalExtended.has(nextDate)) {
				finalExtended.add(nextDate);
				currentDate = nextDate;
			} else {
				break;
			}
		}
	});

	return Array.from(finalExtended).sort();
};

const groupConsecutiveDates = (dates: string[]): string[][] => {
	if (dates.length === 0) return [];

	const sortedDates = dates.sort();
	const groups: string[][] = [];
	let currentGroup = [sortedDates[0]];

	for (let i = 1; i < sortedDates.length; i++) {
		const prevDate = new Date(sortedDates[i - 1]);
		const currentDate = new Date(sortedDates[i]);
		const diffDays = (currentDate.getTime() - prevDate.getTime()) / (1000 * 60 * 60 * 24);

		if (diffDays === 1) {
			currentGroup.push(sortedDates[i]);
		} else {
			groups.push(currentGroup);
			currentGroup = [sortedDates[i]];
		}
	}
	groups.push(currentGroup);

	return groups;
};

const extendedHolidays = extendHolidaysWithWeekends(holidayDates);
const originalHolidaySet = new Set(holidayDates);
const addedDates = extendedHolidays.filter((date) => !originalHolidaySet.has(date));

console.log('추가된 날짜들:', addedDates.length, '개');
console.log(addedDates);

export { addedDates, extendedHolidays, extendHolidaysWithWeekends, groupConsecutiveDates };
