(* Madison Lovett, A01292253
   Mar 10, 2026 *)

type 'a infstream = Cons of 'a * (unit -> 'a infstream)

(* infinite stream of Taylor series terms: x^n / n! *)
let exp_terms x =
  let rec aux index current_term =
    Cons
      ( current_term,
        fun () ->
          let next_term = current_term *. x /. float_of_int index in
          aux (index + 1) next_term )
  in
  aux 1 1.0

(* take stolen from lab *)
let rec take n (Cons (h, t)) = if n <= 0 then [] else h :: take (n - 1) (t ())

(* sum a list of floats *)
let sum = List.fold_left ( +. ) 0.0

(* approximate e^x using num_terms *)
let expo num_terms x = sum (take num_terms (exp_terms x))
