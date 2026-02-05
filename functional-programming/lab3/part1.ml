(* Madison Lovett, A01292253
   Feb 2, 2026 *)

(* Convert number n to list of digits *)
let digits n =
  let rec aux acc n =
    if n = 0 then acc
    else aux (n mod 10 :: acc) (n / 10)
  in
  aux [] n

(* Convert list of digits to number using fold left while also dropping leading 0s *)
let int_of_digits lst =
  List.fold_left (fun acc d -> acc * 10 + d) 0 lst
