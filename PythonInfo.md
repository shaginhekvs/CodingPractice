- Variables in python are like cpp pointers.   
- accessors : don't change state.   
- mutators : change state.  
immutable / mutable instances.  
bool : bool(foo) , empty sequences, 0 are False too. Used in control sequence.  
int: 0b01, 0o57 , 0x7f are literals. int() returns value 0 . arbitary magnitude.  
float: float() , fixed precision, like double in cpp.  
list, tuple, str : seq types. char is just str with len=1.  
list: referential. list() constructs a new object with same data.  
tuple : immutable.(17,) : comma for len 1 tuple.  
str class: immutable seq, escape character 'c:\\python\\'  , multi line using """stuff with newline inside"""  
set and frozenset : set() , only immutable types saved, so frozenset() can be inside set() 
dict: from seq dict([(key1,value1),(key2, value2)])  
logical operators : and , or ( short circuit ) , not  
equality ops : is - true for aliases of same object. a==b , same value in same or diff objects. 
comparison ops : < , <= , >, >= . str compared lexicographically , case sensitively.     
Arithmetic Operators : + - * / // %  . / is true division, returns float, // divisor, % remainder.  q= n//m , r = n % m , then n = q*m + r.  when m +ve , 0<r<m . when m -ve , m < r <=0 . Also extends to floating point such that q is integral floor, and q*m+r = n.  
Bitwise ops : ~&|^<<>>  
sequence ops : s[j] , s[start:stop]  , s+t , k*s , val in s, val not in s. lists del s[j] deletes element. comparison in lexigraphic order. for set, dict, comparisons happen in subset / superset way. 
extended assignment : += , creates new object, but for list, mutates same object.  
parameter passing : by alias mechanism, modifies mutable objects.  
input : returns all before newline as string.  
exception : raise ValueError('x cannot be negative'), TypeError ,.... isinstance, try, except ErrorType as e block is more efficient than if-else raise block.  , can have multiple except statements or except (ValueError, EOFError): in same line.   , there can be finally too.  
iterators : object which accepts next(), iterable generates object using iter() which is iterator. maintain it's own state and reference, if iterable is modified, the iterator reflects that. lazy evaluation is helpful in keys(), values(), range()  .
generators: using yield instead of return, returns an efficient iterator on demand.
Scopes and Napespaces: dir and vars can be used to resolve.  
Random number : python uses Mersenne twister.  
OOPS : Robustness, Adaptability, Reusability. Modularity, Abstraction(interface) using ABC, Encapsulation( use _ before var_name to make it "private").  
Software development : Design -> Responsibilities of actors, Independence over data, Behaviors. CRC cards ( Class responsibility Collaborator) has responsibilities on left, collaborators on right. UML(unified Modeling Language) diagram has class name, vars, function in each row.     
python coding style :   classname style -> camelcase, singular noun. : functions -> lowercase, join by _ . name as a verb, if just returns val, than noun with value. : var names -> lowercase. : consts -> always CAPS using _ to concat.  
Testing strategy: top down, buttom up. Top down used with stubbing, replace input (output from below) with stub. Bottom up : test those who don't call others, also called unit testing. Regression testing.  
Operator Overloading : __add__ , __sub__ , __str__, __hash__ etc must be provided if used.  
Iterator: __next__ returns next element or StopException.  use generator or for class use __len__ & __getitem__.  
Inheritance:  "is a hierarchy" . house (subclass) is a building(superclass). subclass can specialize a behavior, or extend by adding new behavior.  in __init__ of sub, call super.__init__()
Abstract classes have : class ClassName(metaclass=ABSMeta) and @abstractmethod decorator for all abstract functions.  
__slots__ : use when the class's instance vars are already known, to save memory.  
shallow/deep copy: only copy.deepcopy copies fully.  