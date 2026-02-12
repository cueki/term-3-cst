(* Madison Lovett, A01292253
   Feb 4, 2026 *)

(* I am not sure if you wanted comments on each function or not but the code is essentially
   copied from bstree2.ml with slight modifications...*)

type ('k, 'v) kvtree = L | N of 'k * 'v * ('k, 'v) kvtree * ('k, 'v) kvtree

let kvtree_empty = L

let kvtree_is_empty t = t = L

let rec kvtree_find_opt cmp k t =
  match t with
  | L -> None
  | N (k', v, l, _) when cmp k k' < 0 -> kvtree_find_opt cmp k l
  | N (k', _, _, r) when cmp k k' > 0 -> kvtree_find_opt cmp k r
  | N (_, v, _, _) -> Some v

let rec kvtree_add cmp k v t =
  match t with
  | L -> N (k, v, L, L)
  | N (k', v', l, r) when cmp k k' < 0 -> N (k', v', kvtree_add cmp k v l, r)
  | N (k', v', l, r) when cmp k k' > 0 -> N (k', v', l, kvtree_add cmp k v r)
  | N (_, _, l, r) -> N (k, v, l, r)

let rec kvtree_remove_min t =
  match t with
  | L -> failwith "kvtree_remove_min: empty tree"
  | N (k, v, L, r) -> (k, v, r)
  | N (k, v, l, r) ->
    let (min_k, min_v, l') = kvtree_remove_min l in
    (min_k, min_v, N (k, v, l', r))

let rec kvtree_remove cmp k t =
  match t with
  | L -> L
  | N (k', v', l, r) when cmp k k' < 0 -> N (k', v', kvtree_remove cmp k l, r)
  | N (k', v', l, r) when cmp k k' > 0 -> N (k', v', l, kvtree_remove cmp k r)
  | N (_, _, L, r) -> r
  | N (_, _, l, L) -> l
  | N (_, _, l, r) ->
    let (succ_k, succ_v, r') = kvtree_remove_min r in
    N (succ_k, succ_v, l, r')

let kvtree_of_list cmp lst =
  List.fold_left (fun acc (k, v) -> kvtree_add cmp k v acc) L lst
