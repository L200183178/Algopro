package quiz;

/**
 *
 * @author LABRPL-11
 */
public class Pegawai {
    private String Name;
    private String NIM;
    
    public Pegawai () {
        System.out.println ("####Program Kuis####");
    }
    Pegawai (int choice) {
        setPosition (choice);
    }
    public void setPosition (int choice) {
        if(choice==1){
            float Sallary = 2000;
            float Overtime = 50;
            System.out.println("Sallary : $" + Sallary);
            System.out.println("Overtime : $" + Overtime);       
            int rupiah = (int) (Sallary*14500);
            System.out.println("Jika kurs dollar ke rupiah : Rp14.500,00");
            System.out.println("Maka gaji dalam Rupiah :" + rupiah + ",00");
        }
        else {
            if (choice==2){
                float Sallary = 1500;
                float Overtime = 35;
                System.out.println("Sallary : $" + Sallary);
                System.out.println("Overtime : $" + Overtime);
                int rupiah = (int) (Sallary*14500);
                System.out.println("Jika kurs dollar ke rupiah : Rp14.500,00");
                System.out.println("Maka gaji dalam Rupiah : Rp" + rupiah + ",00");
            }
            else {
                System.out.println("Please enter the correct number");
            }
        }
    }
    protected void setName (String newName){
        Name = newName;
    }
    public String getName(){        
        return Name;
    }
    protected void setNIM (String newNIM){
        NIM = newNIM;
    }
    public String getNIM(){
        return NIM;
    }
}
