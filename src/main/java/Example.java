import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;
import java.io.*;

@RestController
@EnableAutoConfiguration
public class Example {

    @RequestMapping("/")
    String home() {

        return runCmd("../deploy/ec2-metadata --all");
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(Example.class, args);
    }

    public String runCmd(String cmd) {
        String out = "";
        try
        {

            Runtime r = Runtime.getRuntime();
            String msg = "", emsg = "";
            //String cmd = "/ec2-metadata --all
            Process p = r.exec(cmd);
            p.waitFor();
            BufferedReader inOut =
                    new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader inErr =
                    new BufferedReader(new InputStreamReader (p.getErrorStream()));
            while ((msg = inOut.readLine()) != null) {
                out += msg;
            }
            while ((emsg = inErr.readLine()) != null)
            {
                out += emsg;
            }
            p.destroy();
        } catch(Exception e) {
            out = e.toString();
        }

        return out;
    }

}