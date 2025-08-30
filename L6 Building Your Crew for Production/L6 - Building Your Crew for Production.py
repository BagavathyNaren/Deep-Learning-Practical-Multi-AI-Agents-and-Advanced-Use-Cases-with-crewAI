#!/usr/bin/env python
# coding: utf-8

# # L6: Building Your Crew for Production

# <p style="background-color:#fff6e4; padding:15px; border-width:3px; border-color:#f5ecda; border-style:solid; border-radius:6px"> ⏳ <b>Note <code>(Kernel Starting)</code>:</b> This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.</p>

# ## Initial Imports

# In[ ]:


# Warning control
import warnings
warnings.filterwarnings('ignore')

# Load environment variables
from helper import load_env
load_env()


# <p style="background-color:#fff6ff; padding:15px; border-width:3px; border-color:#efe6ef; border-style:solid; border-radius:6px"> 💻 &nbsp; <b>Access <code>requirements.txt</code> and <code>helper.py</code> files:</b> 1) click on the <em>"File"</em> option on the top menu of the notebook and then 2) click on <em>"Open"</em>. For more help, please see the <em>"Appendix - Tips and Help"</em> Lesson.</p>

# ## Creating a new project

# In[ ]:


get_ipython().system(' crewai create crew new_project --provider openai')


# ## Setting up the Environment

# <p style="background-color:#fff6e4; padding:15px; border-width:3px; border-color:#f5ecda; border-style:solid; border-radius:6px"> ⏳ <b>Note</code>:</b> The following line might take a few minutes to finish.</p>

# In[ ]:


get_ipython().system(' cd new_project && crewai install')


# ## Setting Environment Variables

# In[ ]:


get_ipython().system(' cat new_project/.env')


# ## Running the Crew

# In[ ]:


get_ipython().system(' cd new_project && crewai run')


# ## Flows CLI - Command Line Interface

# In[ ]:


get_ipython().system(' crewai create flow new_flow')


# In[ ]:


get_ipython().system(' ls -1 new_flow')


# In[ ]:


get_ipython().system(' ls -1 new_flow/src/new_flow/')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




