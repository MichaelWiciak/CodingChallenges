package main

func lexicalOrder(n int) []int {

	output := make([]int, n)

	current := 1
	for i := 0; i < n; i++ {
		output[i] = current

		if current*10 <= n {
			current = current * 10
		} else {
			for current%10 == 9 || current+1 > n {
				current /= 10
			}
			current++
		}
	}
	return output
}
