(* Madison Lovett, A01292253
   Mar 10, 2026 *)

type 'a infstream = Cons of 'a * (unit -> 'a infstream)

(* the infinite filter *)
let rec filter p (Cons (x, tf)) =
  if p x then Cons (x, fun () -> filter p (tf ())) else filter p (tf ())

(* for number in infstream, filter out all multiples beyond x to n *)
let rec sieve (Cons (x, tf)) =
  Cons (x, fun () -> sieve (filter (fun n -> n mod x <> 0) (tf ())))

(* take stolen from lab *)
let rec take n (Cons (h, t)) = if n <= 0 then [] else h :: take (n - 1) (t ())

(* from stolen from lab *)
let rec from n = Cons (n, fun () -> from (n + 1))

(* first 100 primes *)
let first_100 = take 100 (sieve (from 2))
